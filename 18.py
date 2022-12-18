cubes = set()
with (open("18", "r")) as f:
    for line in f.read().splitlines():
        cubes.add(tuple(int(k) for k in line.split(',')))
print(sum(6-sum(k in cubes for k in [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1,
      z), (x, y, z+1), (x, y, z-1)]) for (x, y, z) in cubes))
