# Uses python3
import sys
import random

def swap(a, l, k):
    a[l], a[k] = a[k], a[l]

def partition2(a, l, r):
    x = a[l]
    j = l;
    j1 = 0;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            swap(a, i, j)

    swap(a, l, j)
    return j

def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l + 1

    while(i <= m2):
        if a[i] < x:
            swap(a, i, m1)
            m1 += 1
            i += 1
        elif a[i] > x:
            swap(a, i, m2)
            m2 -= 1
        else:
            i += 1

    return m1, m2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    swap(a, l, k)
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
