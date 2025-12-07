splits = 0
def split(line, i) -> list[int]:
    global splits
    if line[i] == ".": return [i]

    if line[i] == "^":
        splits += 1
        return [i - 1, i + 1]

    raise NotImplemented

def solve1(file):
    global splits
    splits = 0
    with open(file, 'r') as f:
        line = f.readline()
        beams: set[int] = { i for i, _ in enumerate(line) if line[i] == "S" }

        for line in f:
            beams = {
                new_col
                for col in beams
                for new_col in split(line, col)
            }
    return splits



# =============
from collections import defaultdict
def solve2(file):
    global splits
    splits = 0
    with open(file, 'r') as f:
        line = f.readline()
        beams: defaultdict[int, int] = defaultdict()
        beams2 = [ i for i, _ in enumerate(line) if line[i] == "S" ]
        beams[beams2[0]] = 1

        for line in f:
            new_beams = defaultdict(int)
            for col in beams:
                if line[col] == ".":
                    new_beams[col] += beams[col]

                if line[col] == "^":
                    new_beams[col - 1] += beams[col]
                    new_beams[col + 1] += beams[col]
            beams = new_beams

    return sum(beams.values())



print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
