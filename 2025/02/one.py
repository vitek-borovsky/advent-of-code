from itertools import chain
def test_num1(n: int) -> int:
    s = str(n)
    ln = len(s)
    mid = ln // 2

    l = s[:mid]
    r = s[mid:]
    if l == r:
        return n
    return 0

def solve1(file):
    with open(file, 'r') as f:
        line = f.readline().strip()

    ranges = {
        range(
            int(r.split('-')[0]),
            int(r.split('-')[1]) + 1
        )
        for r in line.split(',')
    }

    it = chain(*ranges)

    res = sum(map(test_num1, it,))
    print(f"solve1 {res=}")

def test_num2(n: int) -> int:
    s = str(n)
    ln = len(s)
    for i in range(2, ln + 1):
        if ln / i % 1 != 0: continue

        p_ln = ln // i
        parts = [s[step:step+p_ln] for step in range(0, ln, p_ln)]

        eq = { i == j for i in parts for j in parts }
        if False not in eq:
            return n

    return 0

def solve2(file):
    with open(file, 'r') as f:
        line = f.readline().strip()

    ranges = {
        range(
            int(r.split('-')[0]),
            int(r.split('-')[1]) + 1
        )
        for r in line.split(',')
    }

    it = chain(*ranges)

    res = sum(map(test_num2, it,))
    print(f"solve2 {res=}")


# def solve2(file):

solve1("in.small")
solve1("in")

solve2("in.small")
solve2("in")
