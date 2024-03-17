print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
def is_prime(n):
  if n <= 1:
    return 0  # 0 and 1 are not prime numbers
  elif n <= 3:
    return 1  # 2 and 3 are prime numbers
  elif n % 2 == 0 or n % 3 == 0:
    return 0  # numbers divisible by 2 or 3 are not prime

  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return 0  # if divisible by current or next number, not prime
    i += 6
  return 1  # if not divisible by any number till sqrt(n), it's prime


def main():
  n = int(input("Enter a number to check if it's prime: "))

  if is_prime(n):
    print(f"{n} is a prime number.")
  else:
    print(f"{n} is not a prime number.")


if __name__ == "__main__":
  main()
