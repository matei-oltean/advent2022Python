import re

max_y = 4000000


def merge_and_find_unique(intervals):
    for k in range(len(intervals)):
        interval = sorted(intervals[k])
        i = 0
        while i < len(interval) - 1:
            x1, y1 = interval[i]
            x2, y2 = interval[i+1]
            if y1 >= x2:
                interval[i] = (x1, max(y1, y2))
                interval.pop(i+1)
            else:
                i += 1
        if len(interval) > 1 or interval[0] != (0, max_y):
            x1, x2 = interval[0]
            if x1 != 0:
                return k
            return ((x2+1)*4000000) + k


intervals = [[] for _ in range(max_y+1)]

with (open("15", "r")) as f:
    for line in f.read().splitlines():
        xs, ys, xb, yb = [int(k) for k in re.search(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        d = abs(xs-xb)+abs(ys-yb)
        for y in range(max(ys - d, 0), min(ys + d + 1, max_y)):
            y1, y2 = xs + abs(y - ys) - d, xs - abs(y - ys) + d
            if y1 <= max_y and 0 <= y2 and y1 <= y2:
                intervals[y].append((max(xs + abs(y - ys) - d, 0),
                                    min(xs - abs(y - ys) + d, max_y)))

print(merge_and_find_unique(intervals))
