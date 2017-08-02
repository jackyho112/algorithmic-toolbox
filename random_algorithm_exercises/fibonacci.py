# Uses python3
def calc_fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n <= 3:
    return n - 1

  first_num = second_num = 1
  for num in range(3, n+1):
    first_num, second_num = second_num, first_num + second_num

  return second_num

n = int(input())
print(calc_fib(n))
