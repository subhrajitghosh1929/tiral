import cv2
import numpy as np
import RPi.GPIO as GPI
import time
from threading import Thread

# --- GPIO and Hardware Setup ---
# Pin definitions (using BCM numbering)
GATE_SERVO_PIN = 17
LIGHT_LED_PIN = 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GATE_SERVO_PIN, GPIO.OUT)
GPIO.setup(LIGHT_LED_PIN, GPIO.OUT)

# Setup servo motor for PWM
pwm = GPIO.PWM(GATE_SERVO_PIN, 50)  # 50 Hz frequency for servo
pwm.start(0)

# Function to control the hardware
def activate_hardware():
    print("Car detected! Activating gate and light.")
    
    # 1. Turn on the light
    GPIO.output(LIGHT_LED_PIN, GPIO.HIGH)
    
    # 2. Raise the gate (adjust duty cycle for your specific servo)
    # 7.5 is often a good value for a 90-degree position
    pwm.ChangeDutyCycle(7.5)
    time.sleep(2)  # Wait for the gate to open
    
    # 3. Wait for a moment before closing the gate
    time.sleep(10) # 10 seconds is a good duration for the car to pass
    
    # 4. Lower the gate
    pwm.ChangeDutyCycle(2.5)  # 2.5 is often a good value for a 0-degree position
    time.sleep(2)
    
    # 5. Turn off the light
    GPIO.output(LIGHT_LED_PIN, GPIO.LOW)
    
    print("Hardware deactivated. System is ready for the next car.")

# --- YOLO and Car Detection Setup ---
# Load the YOLO model and class labels
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

car_detected_flag = False

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width, channels = frame.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Process the detections
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and classes[class_id] == "car":  # Only detect cars
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply non-max suppression to remove duplicate boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Check if a car is detected and the flag is not set
        if len(indexes) > 0 and not car_detected_flag:
            car_detected_flag = True
            # Use a separate thread to run the hardware control so it doesn't block the video stream
            hardware_thread = Thread(target=activate_hardware)
            hardware_thread.start()
        
        # Reset the flag after the car has left the frame
        if len(indexes) == 0 and car_detected_flag and not hardware_thread.is_alive():
            car_detected_flag = False
            print("Car has left the frame. System is on standby.")

        # Display the result
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = confidences[i]
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("Car Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Cleanup on exit
    pwm.stop()
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    print("Program terminated and GPIO pins cleaned up.")
