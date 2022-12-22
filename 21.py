def yell(monkeys):
    memo = {}

    def find(name):
        if name in memo:
            return memo[name]
        spl = monkeys[name]
        if len(spl) == 1:
            memo[name] = int(spl[0])
            return int(spl[0])
        first, second = find(spl[0]), find(spl[2])
        match spl[1]:
            case '+': res = first + second
            case '-': res = first - second
            case '/': res = first // second
            case '*': res = first * second
        memo[name] = res
        return res
    return find("root")


monkeys = {}
with (open("21", "r")) as f:
    for line in f.read().splitlines():
        name, instr = line.split(": ")
        monkeys[name] = instr.split(" ")

print(yell(monkeys))
