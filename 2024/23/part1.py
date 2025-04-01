import pdb

def main(filename):
    lines = open(filename).read().splitlines()

    connections = {}

    for line in lines:
        c1, c2 = line.split('-')
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()

        connections[c1].add(c2)
        connections[c2].add(c1)

    triplets = set()
    for c1, entry in connections.items():
        for c2 in entry:
            for c3 in entry:
                # c1 < c2 < c3
                if c2 >= c1 or c3 >= c2:
                    continue

                if c1[0] != 't' and c2[0] != 't' and c3[0] != 't':
                    continue

                if c2 in connections[c1] and c3 in connections[c1] and \
                   c1 in connections[c2] and c3 in connections[c2] and \
                   c1 in connections[c3] and c2 in connections[c3]:
                    triplets.add(( c1, c2, c3 ))
    print(len(triplets))

main("input.small")
main("input")


