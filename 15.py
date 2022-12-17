import re

target_y = 2000000
cannot = set()
occupied = set()
lines = []

with (open("15", "r")) as f:
    for line in f.read().splitlines():
        xs, ys, xb, yb = [int(k) for k in re.search(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        if ys == target_y:
            occupied.add((xs, ys))
        if yb == target_y:
            occupied.add((xb, yb))
        lines.append((xs, ys, xb, yb))

for xs, ys, xb, yb in lines:
    d = abs(xs-xb)+abs(ys-yb)
    if abs(target_y - ys) <= d:
        for x in range(xs + abs(target_y - ys) - d, 1 + xs - abs(target_y - ys) + d):
            if (x, target_y) not in occupied:
                cannot.add(x)
print(len(cannot))
