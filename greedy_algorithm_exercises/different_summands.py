# Uses python3
import sys

def optimal_summands(n):
    remaining = n
    current_num = 1
    summands = []
    while remaining:
        if current_num * 2 >= remaining:
            summands.append(remaining)
            remaining = 0
        else:
            remaining -= current_num
            summands.append(current_num)
            current_num += 1

    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
