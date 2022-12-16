from functools import cmp_to_key

def compare(a, b):
    def compare_elem(l, r):
        if type(l) != type(r):
            if type(l) == int:
                l = [l]
            else:
                r = [r]
        if type(l) == int:
            if l < r:
                return 1
            if l == r:
                return 0
            return -1
        for i in range(len(l)):
            if i >= len(r):
                return -1
            if compare_elem(l[i], r[i]) != 0:
                return compare_elem(l[i], r[i])
        return 1 if len(l) < len(r) else 0
    if compare_elem(a, b) == 1:
        return -1
    return 1


sum = 0
l = []
with (open("13", "r")) as f:
    arr = f.read().split('\n\n')
for i, input in enumerate(arr):
    a, b = [eval(f) for f in input.split('\n')]
    l.append(a)
    l.append(b)
    sum += i + 1 if compare(a, b) == -1 else 0
print(sum)
l.append([[2]])
l.append([[6]])
l.sort(key=cmp_to_key(compare))
print((l.index([[2]])+1)*(l.index([[6]])+1))