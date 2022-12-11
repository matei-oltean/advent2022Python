from collections import deque

items = []
operations = []
rules = []
curTest, toThrow = 0, 0

with (open("11", "r")) as f:
    for line in f.read().splitlines():
        line = line.strip()
        if not line or line.startswith("Monkey"):
            continue
        elif line.startswith("Starting"):
            it = line.split(": ")[1]
            items.append(deque(int(k) for k in it.split(", ")))
        elif line.startswith("Operation"):
            op = line.split("= ")[1].split(" ")
            operations.append(op)
        elif line.startswith("Test"):
            s = line.split(" ")
            curTest = int(s[-1])
        elif line.startswith("If true"):
            s = line.split(" ")
            toThrow = int(s[-1])
        else:
            s = line.split(" ")
            rules.append((curTest, toThrow, int(s[-1])))

counts = [0]*len(items)


def loop(num_iter, decr_stress):
    for _ in range(num_iter):
        for i, val in enumerate(items):
            counts[i] += len(val)
            while len(val):
                item = val.popleft()
                a, op, b = operations[i]
                def o(x, y): return x + y if op == '+' else x * y
                computed = o(item if a == "old" else int(
                    a), item if b == "old" else int(b))
                item = computed//3 if decr_stress else computed
                cond, a, b = rules[i]
                toAppend = a if item % cond == 0 else b
                items[toAppend].append(item)


def part_1():
    loop(20, True)


def part_2():
    loop(10000, False)


part_1()
counts.sort()
print(counts)
print(counts[-1]*counts[-2])
