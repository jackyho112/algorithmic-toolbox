# Uses python3
import sys

def get_majority_element(a, left, right):
    len_a = len(a)
    majority_num = len_a/2
    num_dict = {}

    for num in a:
        if num in num_dict:
            num_dict[num] += 1
            if num_dict[num] > majority_num:
                return num
        else:
            num_dict[num] = 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
