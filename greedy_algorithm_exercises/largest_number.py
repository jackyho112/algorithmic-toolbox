#Uses python3

import sys

def is_greater_or_equal(a, b):
    str_a = str(a)
    str_b = str(b)

    if str_a[0] > str_b[0]:
        return 1
    elif len(str_a) == len(str_b) and a > b:
        return 1
    elif str_a[0] == str_b[0] and len(str_a) < len(str_b):
        return 1
    elif len(str_a) == len(str_b) and a == b:
        return 0

    return -1

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def largest_number(a):
    sorted_a = sorted(a, key=cmp_to_key(is_greater_or_equal), reverse=True)
    res = ""
    for x in sorted_a:
        res += str(x)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
