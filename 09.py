def sign(n):
    if n > 0:
        return 1
    if n == 0:
        return 0
    return -1


def adjacent(x1, y1, x2, y2):
    return max(abs(x1-x2), abs(y1-y2)) <= 1


def move(xt, yt, xh, yh, seen):
    while not adjacent(xt, yt, xh, yh):
        xt, yt = xt + sign(xh - xt), yt + sign(yh - yt)
        seen.add((xt, yt))
    return xt, yt


x, y, xt, yt = 0, 0, 0, 0
visited = set()
visited.add((0, 0))
with (open("09", "r")) as f:
    for line in f.read().splitlines():
        d, dist = line.split(" ")
        dx, dy = 0, 0
        match d:
            case "L":
                dx, dy = -1, 0
            case "R":
                dx, dy = 1, 0
            case "U":
                dx, dy = 0, 1
            case "D":
                dx, dy = 0, -1
        x, y = x + dx*int(dist), y + dy*int(dist)
        xt, yt = move(xt, yt, x, y, visited)
print(len(visited))
