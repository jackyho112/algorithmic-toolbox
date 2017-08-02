# Uses python3
import sys

def get_fibonacci_last_digit(n):
  if n == 0:
    return 0
  elif n <= 3:
    return n - 1

  first_num = second_num = 1
  for num in range(3, n+1):
    first_num, second_num = second_num % 10, (first_num + second_num) % 10

  return second_num

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
