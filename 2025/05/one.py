def solve1(file):
    ranges = []
    with open(file, 'r') as f:
        for l_ in f:
            l = l_.strip()
            if l == "": break
            low, high = l.split("-")
            ranges.append(range(int(low), int(high) + 1))

        is_fresh = lambda id: any((id in rg for rg in ranges))
        return sum((
            is_fresh(int(id))
            for id in f
        ))


### =========
from collections import deque
def merge(rg1: tuple[int, int], rg2: tuple[int, int]) -> list[tuple[int, int]]:
    print(f"Merging {rg1=} {rg2=}", end='\t')
    if rg1[1] >= rg2[0]:
        print(f"merged={(rg1[0], rg2[1])}")
        return [(rg1[0], max(rg1[1], rg2[1]))]

    print("not_merged")
    return [rg1, rg2]


def solve2(file):
    ranges: deque[tuple[int, int]] = deque()
    with open(file, 'r') as f:
        for l_ in f:
            l = l_.strip()
            if l == "": break
            low, high = l.split("-")
            ranges.append((int(low), int(high) + 1))

    ranges = deque(sorted(list(ranges)))

    sm = 0
    consume_rg = lambda rg: rg[1] - rg[0]
    main_rg = ranges.popleft()
    while len(ranges) > 0:
        cur_rg = ranges.popleft()
        answ = merge(main_rg, cur_rg)
        if len(answ) == 1:
            main_rg = answ[0]
            continue

        sm += consume_rg(answ[0])
        main_rg = answ[1]

    sm += consume_rg(main_rg)
    return sm

print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
