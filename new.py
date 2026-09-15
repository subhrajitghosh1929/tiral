import mysql.connector

class HospitalBedManagement:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="SUBH",  # Change as per your MySQL credentials
            password="#GODGAMERPR01#",  # Change as per your MySQL credentials
            database="hospital_db"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Beds (
            bed_id INT AUTO_INCREMENT PRIMARY KEY,
            ward VARCHAR(50),
            status ENUM('Available', 'Occupied') DEFAULT 'Available'
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patients (
            patient_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            disease VARCHAR(255),
            bed_id INT,
            admission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (bed_id) REFERENCES Beds(bed_id) ON DELETE SET NULL
        );
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Billing (
            bill_id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            total_amount DECIMAL(10,2),
            payment_status ENUM('Pending', 'Paid') DEFAULT 'Pending',
            FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE
        );
        """)
        
        self.conn.commit()

    def add_bed(self):
        ward = input("Enter ward name: ")
        self.cursor.execute("INSERT INTO Beds (ward) VALUES (%s)", (ward,))
        self.conn.commit()
        print("Bed added successfully.")

    def admit_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter disease: ")
        self.cursor.execute("SELECT bed_id FROM Beds WHERE status = 'Available' LIMIT 1")
        bed = self.cursor.fetchone()
        if bed:
            bed_id = bed[0]
            self.cursor.execute("INSERT INTO Patients (name, age, disease, bed_id) VALUES (%s, %s, %s, %s)", (name, age, disease, bed_id))
            patient_id = self.cursor.lastrowid
            self.cursor.execute("UPDATE Beds SET status = 'Occupied' WHERE bed_id = %s", (bed_id,))
            self.cursor.execute("INSERT INTO Billing (patient_id, total_amount, payment_status) VALUES (%s, %s, 'Pending')", (patient_id, 5000))
            self.conn.commit()
            print("Patient admitted successfully.")
        else:
            print("No available beds.")

    def discharge_patient(self):
        patient_id = int(input("Enter patient ID to discharge: "))
        self.cursor.execute("SELECT bed_id FROM Patients WHERE patient_id = %s", (patient_id,))
        bed = self.cursor.fetchone()
        if bed:
            bed_id = bed[0]
            self.cursor.execute("DELETE FROM Patients WHERE patient_id = %s", (patient_id,))
            self.cursor.execute("UPDATE Beds SET status = 'Available' WHERE bed_id = %s", (bed_id,))
            self.conn.commit()
            print("Patient discharged successfully.")
        else:
            print("Patient not found.")

    def generate_bill(self):
        patient_id = int(input("Enter patient ID for billing: "))
        self.cursor.execute("SELECT total_amount, payment_status FROM Billing WHERE patient_id = %s", (patient_id,))
        bill = self.cursor.fetchone()
        if bill:
            print(f"Total Amount: {bill[0]}")
            print(f"Payment Status: {bill[1]}")
            if bill[1] == 'Pending':
                confirm = input("Do you want to mark the bill as Paid? (yes/no): ")
                if confirm.lower() == 'yes':
                    self.cursor.execute("UPDATE Billing SET payment_status = 'Paid' WHERE patient_id = %s", (patient_id,))
                    self.conn.commit()
                    print("Payment completed successfully.")
        else:
            print("No billing record found for the patient.")

    def view_beds(self):
        self.cursor.execute("SELECT * FROM Beds")
        for row in self.cursor.fetchall():
            print(row)

    def view_patients(self):
        self.cursor.execute("SELECT * FROM Patients")
        for row in self.cursor.fetchall():
            print(row)

    def close_connection(self):
        self.conn.close()

    def menu(self):
        while True:
            print("\nHospital Bed Management System")
            print("1. Add Bed")
            print("2. Admit Patient")
            print("3. Discharge Patient")
            print("4. View Beds")
            print("5. View Patients")
            print("6. Generate Bill")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_bed()
            elif choice == "2":
                self.admit_patient()
            elif choice == "3":
                self.discharge_patient()
            elif choice == "4":
                self.view_beds()
            elif choice == "5":
                self.view_patients()
            elif choice == "6":
                self.generate_bill()
            elif choice == "7":
                self.close_connection()
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    hospital = HospitalBedManagement()
    hospital.menu()
