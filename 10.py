def drawAndSum(i, res):
    if (i - 1) % 40 == 0:
        print()
    if abs((i - 1) % 40 - res) <= 1:
        print('\u2588', end=" ")
    else:
        print(' ', end=" ")
    if i % 40 == 20:
        return res*i
    return 0


res, sol = 1, 0
i = 1
with (open("10", "r")) as f:
    for line in f.read().splitlines():
        sol += drawAndSum(i, res)
        if line != "noop":
            i += 1
            sol += drawAndSum(i, res)
            _, a = line.split(" ")
            res += int(a)
        i += 1
print()
print(sol)
