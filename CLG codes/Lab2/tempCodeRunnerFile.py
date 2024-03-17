print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def is_armstrong_number(number):
  # Convert number to string to count digits
  num_str = str(number)
  num_digits = len(num_str)

  # Calculate sum of digits raised to the power of num_digits
  armstrong_sum = sum(int(digit)**num_digits for digit in num_str)

  # Check if the number is equal to the sum
  return armstrong_sum == number


def main():
  number = int(input("Enter a number to check if it's an Armstrong number: "))

  if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
  else:
    print(f"{number} is not an Armstrong number.")


if __name__ == "__main__":
  main()
