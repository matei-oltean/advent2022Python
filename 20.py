def mix(cups, mult=1, rounds=1):
    cups = [v*mult for v in cups]
    moving_cups = list(enumerate(cups))
    for _ in range(rounds):
        for i, k in enumerate(cups):
            pos = moving_cups.index((i, k))
            moving_cups.pop(pos)
            new_pos = (pos + k + len(moving_cups)) % len(moving_cups)
            moving_cups.insert(new_pos, (i, k))
    zero = moving_cups.index((cups.index(0), 0))
    print(sum(moving_cups[(zero + k) % len(moving_cups)][1]
          for k in [1000, 2000, 3000]))


with (open("20", "r")) as f:
    cups = [int(k) for k in f.readlines()]

mix(cups)
mix(cups, 811589153, 10)
