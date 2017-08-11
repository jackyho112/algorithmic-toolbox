# Uses python3
import sys
import math

def binary_search(num, arr, min_index, max_index):
    if (max_index - min_index) > 2:
        guess = math.floor((max_index + min_index) / 2)
        guessed_num = arr[guess]

        if guessed_num == num:
            return guess
        elif guessed_num > num:
            return binary_search(num, arr, min_index, guess - 1)
        elif guessed_num < num:
            return binary_search(num, arr, guess + 1, max_index)

    for i in range(min_index, max_index + 1):
        if arr[i] == num:
            return i

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(x, a, 0, len(a) - 1), end = ' ')
