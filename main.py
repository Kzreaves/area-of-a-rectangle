length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
area = area/2

print("The area of the rectangle is:", area)

try:
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
except ValueError:
  print("Invalid input. Please enter a number.")


area = length * width

