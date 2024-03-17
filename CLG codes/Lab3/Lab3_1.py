print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def factorial(n):
  # Base case: factorial of 0 is 1
  if n == 0:
    return 1
  # Recursive case: factorial of n is n * factorial(n-1)
  return n * factorial(n - 1)


def nCr(n, r):
  return factorial(n) // (factorial(r) * factorial(n - r))


def nPr(n, r):
  return factorial(n) // factorial(n - r)


def main():
  n = int(input("Enter the value of n: "))
  r = int(input("Enter the value of r: "))

  if n < r:
    print("Invalid input. n should be greater than or equal to r.")
    return

  combination = nCr(n, r)
  permutation = nPr(n, r)

  print(f"nCr (Combination): {combination}")
  print(f"nPr (Permutation): {permutation}")


if __name__ == "__main__":
  main()
