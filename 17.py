def is_valid(form, map):
    for x, y in form:
        if x < 0 or x > 6:
            return False
        if y <= 0:
            return False
        if (x, y) in map:
            return False
    return True


def spawn(form, map, bottom):
    return [(x + 2, y+bottom+4) for (x, y) in form]


def push(form, dir):
    match dir:
        case '>': return [(x+1, y) for (x, y) in form]
        case '<': return [(x-1, y) for (x, y) in form]
    return [(x, y-1) for (x, y) in form]


forms = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

dir = ''
map = set()
with (open("17", "r")) as f:
    dir = f.read()
round = -1
bottom = 0
for k in range(2022):
    form = spawn(forms[k % len(forms)], map, bottom)
    while True:
        round += 1
        new_form = push(form, dir[round % len(dir)])
        if is_valid(new_form, map):
            form = new_form
        new_form = push(form, 'down')
        if is_valid(new_form, map):
            form = new_form
        else:
            for (x, y) in form:
                map.add((x, y))
                bottom = max(y, bottom)
            break

print(max(y for (_, y) in map))
