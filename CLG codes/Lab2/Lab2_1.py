print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def find_greatest_number(num1, num2, num3):
  return max(num1, num2, num3)


def main():
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  num3 = float(input("Enter the third number: "))

  greatest_number = find_greatest_number(num1, num2, num3)

  print(
      f"The greatest number among {num1}, {num2}, and {num3} is: {greatest_number}"
  )


if __name__ == "__main__":
  main()
