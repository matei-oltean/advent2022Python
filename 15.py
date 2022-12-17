import re

target_y = 2000000
intervals = []
to_ignore = set()

with (open("15", "r")) as f:
    for line in f.read().splitlines():
        xs, ys, xb, yb = [int(k) for k in re.search(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        if ys == target_y:
            to_ignore.add(xs)
        if yb == target_y:
            to_ignore.add(xb)
        d = abs(xs-xb)+abs(ys-yb)
        if abs(target_y - ys) <= d:
            intervals.append((xs + abs(target_y - ys) - d,
                             xs - abs(target_y - ys) + d))

intervals.sort(key=lambda x: (x[0], x[1]))
i = 0
while i < len(intervals) - 1:
    x1, y1 = intervals[i]
    x2, y2 = intervals[i+1]
    if y1 >= x2:
        intervals[i] = (x1, max(y1, y2))
        intervals.pop(i+1)
    else:
        i += 1
print(sum(b - a + 1 for (a, b) in intervals) - len(to_ignore))
