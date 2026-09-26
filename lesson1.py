# Stores your name, age, height in meters (e.g. 1.75), and whether you are a student (True or False) in four variables.
# Prints a small info card using f-strings.
# Prints the type of each variable.
# Includes at least one comment.

name = "Johny Alam"  # String variable to store the name
age = 30  # Integer variable to store the age
height = 1.75  # Float variable to store the height in meters
is_student = True  # Boolean variable to indicate if the person is a student

print("===== Info Card =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} m")
print(f"Is Student: {is_student}")

print("=====================")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))