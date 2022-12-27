def to_base_10(n):
    pow = 1
    res = 0
    for s in reversed(n):
        match s:
            case '1': res += pow
            case '2': res += 2*pow
            case '-': res -= pow
            case '=': res -= 2*pow
        pow *= 5
    return res


def to_base_5(n):
    res = ''
    while n > 0:
        r = n % 5
        n //= 5
        if 0 <= r <= 2:
            res += str(r)
            continue
        n += 1
        r = r-5
        if r == -2:
            res += '='
        else:
            res += '-'
    return res[::-1]


sum = 0
with (open("25", "r")) as f:
    for line in f.read().splitlines():
        sum += to_base_10(line)
print(to_base_5(sum))
