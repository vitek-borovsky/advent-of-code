def solve_bat_rec(line: str, pos: int) -> tuple[int, int]:
    if pos == len(line) - 2:
        return (int(line[-2]), int(line[-1]))

    val = int(line[pos])
    prev = solve_bat_rec(line, pos + 1)

    if val >= prev[0]:
        return val, max(prev)

    return prev

def solve_bat(line: str) -> int:
    res = solve_bat_rec(line, 0)
    return 10*res[0] + res[1]


def solve1(file):
    with open(file, 'r') as f:
        return sum((
            solve_bat(line.strip())
            for line in f
        ))

########################
N = 12
def solve_bat_rec2(line: str, pos: int) -> list[int]:
    if pos == len(line) - N:
        return [ int(line[-n]) for n in range(N, 0, -1) ]

    val = int(line[pos])
    prev = solve_bat_rec2(line, pos + 1)

    carry = val
    for i in range(N):
        if carry >= prev[i]:
            carry, prev[i] = prev[i], carry
        else:
            break

    # if val >= prev[0]:
    #     return val, max(prev)

    return prev

def solve_bat2(line: str) -> int:
    res = solve_bat_rec2(line, 0)
    digits = ( str(d) for d in res )
    num = ''.join(digits)
    return int(num)


def solve2(file):
    with open(file, 'r') as f:
        return sum((
            solve_bat2(line.strip())
            for line in f
        ))

# def solve2(file):
print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
