from uf import UnionFind

from math import prod
from collections import Counter
INF = 10**1000
dist = lambda p1, p2: sum(((e1 - e2) ** 2 for e1, e2 in zip(p1, p2)))

def solve1(file, conns: int):
    points = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            point: tuple[int, int, int] = tuple(map(int, line.strip().split(',')))
            points.append(point)

    dists = [ (dist(p1, p2), i, j)
        for i, p1 in enumerate(points)
        for j, p2 in enumerate(points)
        if i > j ]

    pairs: list[tuple[int, int, int]] = sorted(dists)
    uf = UnionFind(len(points))

    for _, i, j in pairs[:conns]:
        uf.union(i, j)

    c = Counter(uf.values())
    print(c)
    return prod(val for _, val in c.most_common(3))

# =============
def solve2(file):
    points = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            point: tuple[int, int, int] = tuple(map(int, line.strip().split(',')))
            points.append(point)

    dists = [ (dist(p1, p2), i, j)
        for i, p1 in enumerate(points)
        for j, p2 in enumerate(points)
        if i > j ]

    pairs: list[tuple[int, int, int]] = sorted(dists)
    uf = UnionFind(len(points))

    res = 0
    for _, i, j in pairs:
        if uf[i] == uf[j]: continue
        uf.union(i, j)
        p1, p2 = points[i], points[j]
        res = p1[0] * p2[0]

    return res



print(solve1("in.small", 10))
print(solve1("in", 1000))

print(solve2("in.small"))
print(solve2("in"))
