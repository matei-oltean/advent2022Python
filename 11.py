from collections import deque

items = []
operations = []
rules = []
curTest, toThrow = 0, 0
prod = 1

with (open("11", "r")) as f:
    for line in f.read().splitlines():
        line = line.strip()
        if not line or line.startswith("Monkey"):
            continue
        elif line.startswith("Starting"):
            it = line.split(": ")[1]
            items.append(deque(int(k) for k in it.split(", ")))
        elif line.startswith("Operation"):
            a, op, b = line.split("= ")[1].split(" ")
            def o(x, y): return x + y if op == '+' else x * y
            operations.append(lambda x: o(x if a == "old" else int(
                a), x if b == "old" else int(b)))
        elif line.startswith("Test"):
            s = line.split(" ")
            curTest = int(s[-1])
            prod *= curTest
        elif line.startswith("If true"):
            s = line.split(" ")
            toThrow = int(s[-1])
        else:
            s = line.split(" ")
            rules.append(lambda x: toThrow if x % curTest == 0 else int(s[-1]))
counts = [0]*len(items)


def loop(num_iter, decr_stress):
    for _ in range(num_iter):
        for i, val in enumerate(items):
            counts[i] += len(val)
            while len(val):
                item = val.popleft()
                computed = operations[i](item)
                item = computed//3 if decr_stress else computed
                item = item % prod
                toAppend = rules[i](item)
                items[toAppend].append(item)


def part_1():
    loop(20, True)


def part_2():
    loop(10000, False)


part_2()
counts.sort()
print(counts[-1]*counts[-2])
