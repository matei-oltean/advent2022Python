def sign(n):
    if n > 0:
        return 1
    if n == 0:
        return 0
    return -1


def adjacent(x1, y1, x2, y2):
    return max(abs(x1-x2), abs(y1-y2)) <= 1


def move(knots, seen):
    moved = True
    while moved:
        moved = False
        for i in range(1, len(knots)):
            (xt, yt), (xh, yh) = knots[i], knots[i-1]
            if not adjacent(xt, yt, xh, yh):
                moved = True
                knots[i] = xt + sign(xh - xt), yt + sign(yh - yt)
            if i == 1:
                seen[0].add((xt, yt))
            elif i == 9:
                seen[1].add((xt, yt))


knots = [(0, 0)]*10
visited = [set(), set()]
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
        x, y = knots[0]
        knots[0] = x + dx*int(dist), y + dy*int(dist)
        move(knots, visited)
print(len(visited[0]))
print(len(visited[1]))
