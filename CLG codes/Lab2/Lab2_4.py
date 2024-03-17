print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def cube_root(number):
  return number**(1 / 3)


def main():
  number = float(input("Enter a number to find its cube root: "))
  if number < 0:
    print("Cube root is not defined for negative numbers.")
  else:
    result = cube_root(number)
    print(f"The cube root of {number} is: {result:.6f}")


if __name__ == "__main__":
  main()
