print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def check_odd_even(number):
  if number % 2 == 0:
    return "even"
  else:
    return "odd"


def main():
  number = int(input("Enter a number: "))
  result = check_odd_even(number)
  print(f"The number {number} is {result}.")


if __name__ == "__main__":
  main()
