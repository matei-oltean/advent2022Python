from collections import defaultdict
import math


def get_bounds(pos):
    min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
    for x, y in pos:
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)
    return min_x, max_x, min_y, max_y


def print_pos(pos):
    positions = set(pos)
    min_x, max_x, min_y, max_y = get_bounds(pos)
    for j in range(max_y, min_y - 1, -1):
        print(''.join('#' if (i, j)
              in positions else '.' for i in range(min_x, max_x + 1)))
    print()


def get_pos(move):
    match move:
        case 'S': return [(0, -1), (1, -1), (-1, -1)], (0, -1)
        case 'N': return [(0, 1), (1, 1), (-1, 1)], (0, 1)
        case 'W': return [(-1, -1), (-1, 0), (-1, 1)], (-1, 0)
        case 'E': return [(1, -1), (1, 0), (1, 1)], (1, 0)


def do_round(pos, moves):
    elf_moved = False
    positions = set(pos)
    proposed_move = [(0, 0)]*len(pos)
    should_move = [False]*len(pos)
    count_proposed = defaultdict(lambda: 0)
    for i, (x, y) in enumerate(pos):
        elf_moves = False
        for dx, dy in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
            if (x+dx, y+dy) in positions:
                elf_moves = True
                break
        if not elf_moves:
            continue
        for move in moves:
            check, proposed = get_pos(move)
            alone = True
            for dx, dy in check:
                if (x+dx, y+dy) in positions:
                    alone = False
                    break
            if not alone:
                continue
            new_move = x+proposed[0], y+proposed[1]
            proposed_move[i] = new_move
            count_proposed[new_move] += 1
            should_move[i] = True
            break
    for i, move in enumerate(proposed_move):
        if should_move[i] and count_proposed[move] == 1:
            pos[i] = move
            elf_moved = True
    moves.append(moves.pop(0))
    return elf_moved


pos = []
with (open("23", "r")) as f:
    for j, line in enumerate(f.read().splitlines()):
        for i, v in enumerate(line):
            if v == '#':
                pos.append((i, -j))
moves = ['N', 'S', 'W', 'E']

for _ in range(10):
    do_round(pos, moves)
min_x, max_x, min_y, max_y = get_bounds(pos)
print((max_x-min_x + 1)*(max_y-min_y + 1) - len(pos))

elf_moved = True
i = 10
while elf_moved:
    elf_moved = do_round(pos, moves)
    i += 1
print(i)
