# Uses python3
import sys
import math

def change(m, num):
    return math.floor(m/num)

def get_change(m):
    remaining = m
    num_of_coins = 0

    for coin in [10, 5, 1]:
        num = change(remaining, coin)
        remaining -= (num * coin)
        num_of_coins += num

    return num_of_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
