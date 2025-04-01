import pdb

def is_connected(st: tuple[str], new_ver: str, connections: dict[str, set[str]]):
    for c1 in st:
        if c1 not in connections[new_ver] or new_ver not in connections[c1]:
            return False
    return True


def step(sets: set[tuple[str]], connections: dict[str, set[str]]) -> set[tuple[str]]:
    new_sets = set()
    for st in sets:
        for ver in connections.keys() - st:
            if is_connected(st, ver, connections):
                new_sets.add(tuple(sorted({*st,  ver })))

    return new_sets

def main(filename):
    lines = open(filename).read().splitlines()
    connections: dict[str, set[str]] = {}
    for line in lines:
        c1, c2 = line.split('-')
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()

        connections[c1].add(c2)
        connections[c2].add(c1)



    sets: set[tuple[str]] = { ( ver, ) for ver in connections.keys() }
    for i in range(1, 10000):
        print(f"ITER: {i}, size: {len(sets)}")

        # pdb.set_trace()
        new_sets = step(sets, connections)
        if len(new_sets) == 0:
            break
        sets = new_sets
    print(",".join(list(sets)[0]))

main("input.small")
main("input")
