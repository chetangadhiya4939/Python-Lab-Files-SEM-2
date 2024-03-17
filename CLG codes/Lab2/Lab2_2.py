print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def display_multiplication_table(number):
  print(f"Multiplication table of {number}:")
  for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


def main():
  num = int(input("Enter an integer to display its multiplication table: "))
  display_multiplication_table(num)


if __name__ == "__main__":
  main()
