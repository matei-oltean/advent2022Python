pos = ['.']
structure = {}
sizes = {}
with (open("07", "r")) as f:
    for line in f.read().splitlines():
        if line[0] == '$':
            if line[2] == 'c':
                nextDir = line[len('$ cd '):]
                if nextDir == '.':
                    pos = ['.']
                elif nextDir == '..':
                    pos = pos[:-1]
                else:
                    pos.append(nextDir)
            continue
        [a, b] = line.split(' ')
        cur = '/'.join(pos)
        if cur not in structure:
            structure[cur] = set()
        if a == 'dir':
            structure[cur].add((cur + '/' + b, 0))
        else:
            structure[cur].add((b, int(a)))


def compute(key):
    if key in sizes:
        return sizes[key]
    size = 0
    for (a, b) in structure[key]:
        if b > 0:
            size += b
        else:
            size += compute(a)
    sizes[key] = size
    return size


res = 0
for key in structure:
    if compute(key) <= 100000:
        res += compute(key)

ok = -1
availableSize = 70000000 - sizes['.//']
needed = 30000000 - availableSize
for key in structure:
    if compute(key) >= needed and (compute(key) < ok or ok < 0):
        ok = compute(key)
print(res)
print(ok)
