# Uses python3
import sys

def optimal_sequence(target):
    trees = [
        [[0,target]]
    ]
    level = 0
    number_reached = target
    sequence = []

    while number_reached > 1:
        level_nums = []

        for index, n in enumerate(trees[level]):
            num = n[1]

            if num % 3 == 0:
                level_nums.append([index, num // 3])
            else:
                if num % 2 == 0:
                    level_nums.append([index, num // 2])

                level_nums.append([index, num - 1])

        item = min(level_nums, key=lambda x: x[1])
        number_reached = item[1]
        trees.append(level_nums)
        level += 1

        if number_reached == 1:
            num = item[1]
            while level:
                sequence.append(num)
                level -= 1
                item = trees[level][item[0]]
                num = item[1]

    sequence.append(target)

    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
