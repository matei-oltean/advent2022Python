def in_bounds(x, y, map, depth):
    if y == depth + 2:
        return False
    return (x, y) not in map


def fall(map, depth, bottomless):
    x, y = 500, 0
    can_move = True
    while can_move:
        if bottomless and y > depth:
            return x, y
        can_move = False
        if in_bounds(x, y + 1, map, depth):
            y = y + 1
            can_move = True
        elif in_bounds(x-1, y+1, map, depth):
            x, y = x-1, y+1
            can_move = True
        elif in_bounds(x+1, y+1, map, depth):
            x, y = x+1, y+1
            can_move = True
    return x, y


def simulate_fall(map, depth, bottomless):
    res = 0
    while True:
        x, y = fall(map, depth, bottomless)
        if bottomless and y > depth:
            return res
        if y == 0:
            return res + 1
        res += 1
        map.add((x, y))


map = set()
depth = 0
with (open("14", "r")) as f:
    for line in f.read().splitlines():
        segments = [[int(l) for l in k.split(',')] for k in line.split(' -> ')]
        x, y = segments[0]
        map.add((x, y))
        if y > depth:
            depth = y
        for _, (i, j) in enumerate(segments[1:]):
            for ii in range(min(i, x), max(i, x) + 1):
                for jj in range(min(j, y), max(j, y) + 1):
                    map.add((ii, jj))
            x, y = i, j
            if y > depth:
                depth = y

# print(simulate_fall(map, depth, False))
print(simulate_fall(map, depth, False))
