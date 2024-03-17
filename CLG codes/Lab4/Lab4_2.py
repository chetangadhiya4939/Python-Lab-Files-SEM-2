print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def slope(t1, t2, t3, t4):
  return (t2 - t4) / (t1 - t3)


print("Enter the Points ----")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("\n")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print("\n")
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))
print("\n")

s1 = slope(x1, y1, x2, y2)
s2 = slope(x2, y2, x3, y3)
s3 = slope(x3, y3, x1, y1)

if s1 == s2 and s2 == s3:
  print("The points are collinear")
else:
  print("The points are not collinear")
