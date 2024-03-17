print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def count_a_frequency(input_string):
  count = 0
  for char in input_string:
    if char == 'a' or char == 'A':
      count += 1
  return count


def main():
  input_string = input("Enter a string: ")
  frequency = count_a_frequency(input_string)
  print(f"The frequency of 'a'/'A' in the input string is: {frequency}")


if __name__ == "__main__":
  main()
