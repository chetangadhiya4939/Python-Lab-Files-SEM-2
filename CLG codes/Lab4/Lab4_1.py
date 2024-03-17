import math
print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
print("Write the Co-ordinates of the Circle")
x = int(input("x = "))
y = int(input("y = "))

print("Write the Radius of the Circle")
r = int(input("r = "))

print("Write the Co-ordinates of the Point")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

d = math.sqrt(pow((x1 - x), 2) + pow((y1 - y), 2))

if d < r:
  print("Point is inside the Circle")
elif d > r:
  print("Point is outside the Circle")
else:
  print("Point is on the Circle")
