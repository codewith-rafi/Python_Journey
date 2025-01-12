#typecast (string, integer, float, boolean)

name = "Rafi"
age = 22
gpa = 3.5
student = True

# Explicit - Manually

# age = float(age)
# print(type(age))

# gpa = int(gpa)
# print(type(gpa))

# age = bool(age)
# print(type(age))

# student = str(student)
# print(type(student))

# name = bool(name)
# print(type(name))

# Implicit - Automatic

x = 2
y = 2.0

x = x / y

print(x)

# Here the result converted to floating number!