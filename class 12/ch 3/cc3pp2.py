def calculate_volume(length = 5, width = 3, height = 2):
    return length * width * height

default_volume = calculate_volume()
print("Volume of the box with default values:", default_volume)

v = calculate_volume(10, 7, 15)
print("Volume of the box with default values:", v)

a = calculate_volume(length = 23, height = 6)
print("Volume of the box with default values:", a)

b = calculate_volume(width = 19)
print("Volume of the box with default values:", b)
