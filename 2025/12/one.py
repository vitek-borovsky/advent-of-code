def solve1(file):
    with open(file, 'r') as f:
        text = ''.join(f.readlines()).strip()
    sections = text.split('\n\n')
    presents = sections[:-1]
    problems = sections[-1].split('\n')

    present_sizes = {
        i: sum((c == "#") for c in row)
        for i, row in enumerate(presents)
    }
    def solve_problem(prob) -> bool:
        dim, counts = prob.split(': ')
        x, y = dim.split('x')
        pres_area = sum((present_sizes[i] * int(cnt) for i,cnt in enumerate(counts.split(' '))))
        return int(x) * int(y) >= pres_area

    return sum((solve_problem(p) for p in problems))

#############################################################
def solve2(file):
    pass

print(solve1("in.small"))
print(solve1("in"))

# print(solve2("in.small2"))
# print(solve2("in"))
