# Uses python3
import sys

def gcd(a, b):
    result_arr = sorted([a, b])
    result_arr.reverse()

    first_num = result_arr[0]
    second_num = result_arr[1]

    while second_num:
      first_num, second_num = second_num, first_num % second_num

    return first_num

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
