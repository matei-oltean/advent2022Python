dirs = (0, 1), (1, 0), (0, -1), (-1, 0)


def inBounds(i, j, forest):
    return 0 <= i < len(forest) and 0 <= j < len(forest[0])


def count(i, j, v, prev, seen):
    if v > prev:
        seen.add((i, j))
    return max(v, prev)


def countScore(forest, i, j):
    a = 1
    for di, dj in dirs:
        k = 1
        aa = 0
        while inBounds(i+k*di, j+k*dj, forest):
            aa += 1
            if forest[i][j] <= forest[i+k*di][j+k*dj]:
                break
            k += 1
        a *= aa
    return a


forest = []
with (open("08", "r")) as f:
    for line in f.read().splitlines():
        forest.append([int(i) for i in line])
seen = set()

for i, line in enumerate(forest):
    prev = -1
    for j, v in enumerate(line):
        prev = count(i, j, v, prev, seen)
    prev = -1
    for j, v in reversed(list(enumerate(line))):
        prev = count(i, j, v, prev, seen)

for j in range(len(forest[0])):
    prev = -1
    for i, v in enumerate(forest):
        prev = count(i, j, v[j], prev, seen)
    prev = -1
    for i, v in reversed(list(enumerate(forest))):
        prev = count(i, j, v[j], prev, seen)

print(len(seen))
print(max(countScore(forest, i, j) for i, j in seen if i != 0 and j !=
      0 and i != len(forest) - 1 and j != len(forest[0]) - 1))
