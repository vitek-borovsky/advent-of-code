import math
def solve1(file):
    def get_non_empty_gen(s):
        return ( c for c in s.split(' ') if c.strip() != '' )

    def conc(l: list[list[int]], s: str):
        for i, num in enumerate(get_non_empty_gen(s)):
            l[i].append(int(num))

    def ev(l: list[int], op: str):
        if op == '+': return sum(l)
        if op == '*': return math.prod(l)
        raise NotImplemented


    with open(file, 'r') as f:
        line = f.readline().strip()
        problems = [ [ int(num) ] for num in get_non_empty_gen(line) ]

        while (line := f.readline().strip())[0] in '0123456789':
            conc(problems, line)

        return sum((
            ev(l, op) for l, op in zip(problems, get_non_empty_gen(line))
        ))


# =============
def solve2(file):
    with open(file, 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    nums = [ list(line) for line in lines[:-1] ]
    [ l.append(' ') for l in nums ]

    ops = (sum if op == "+" else math.prod for op in lines[-1].split() )

    sm = 0
    operands = []
    for col in range(len(nums[0])):
        line = "".join((
            c.replace(' ', '')
            for row in range(len(nums))
            for c in nums[row][col]
        ))

        if line == '':
            sm += next(ops)(operands)
            operands = []
            continue

        operands.append(int(line))

    return sm



print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
