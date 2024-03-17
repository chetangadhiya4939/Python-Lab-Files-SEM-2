print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def isPal(input_string):
  # Convert input string to lowercase and remove spaces
  input_string = input_string.lower().replace(" ", "")

  # Check if the string is equal to its reverse
  return input_string == input_string[::-1]


def main():
  input_string = input("Enter a string: ")

  if isPal(input_string):
    print("The input string is a palindrome.")
  else:
    print("The input string is not a palindrome.")


if __name__ == "__main__":
  main()
