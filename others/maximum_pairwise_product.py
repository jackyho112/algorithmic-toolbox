# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

largest_two = sorted(a)[len(a)-2:]
result = largest_two[0]*largest_two[1]

print(result)
