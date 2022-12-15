from collections import deque


def bfs(arr, start, end):
    boundary = deque()
    for x, y in start:
        boundary.append((x, y, 0))
    seen = set()
    while True:
        i, j, dist = boundary.popleft()
        if (i, j) == end:
            return dist
        if (i, j) in seen:
            continue
        seen.add((i, j))
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= i + di < len(arr) and 0 <= j + dj < len(arr[i + di]) and (i+di, j+dj) not in seen and arr[i][j] + 1 >= arr[i+di][j+dj]:
                boundary.append((i+di, j+dj, dist + 1))


lowest = []
with (open("12", "r")) as f:
    arr = [[ord(c) for c in line] for line in f.read().splitlines()]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == ord('a'):
            lowest.append((i, j))
        if arr[i][j] == ord('S'):
            start = i, j
            lowest.append((i, j))
            arr[i][j] = ord('a')
        if arr[i][j] == ord('E'):
            end = i, j
            arr[i][j] = ord('z')

print(bfs(arr, [start], end))
print(bfs(arr, lowest, end))
