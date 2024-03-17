import math
print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")

def calculate_circle_area(radius):
  return math.pi * radius**2


def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(
    f"The area of the circle with radius {radius} is {area:.2f} square units."
    )


if __name__ == "__main__":
    main()
