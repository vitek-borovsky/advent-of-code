import pdb
def get_towels(line):
    return [ towel.strip() for towel in line.split(',') ]

def fits(pattern, towel, inx):
    if inx + len(towel) > len(pattern):
        return False
    return pattern[inx:inx + len(towel)] == towel

def can_arrange(pattern, towels, inx = 0) -> int:
    if inx == len(pattern): return 1
    for towel in towels:
        if fits(pattern, towel, inx):
            if can_arrange(pattern, towels, inx + len(towel)):
                return 1
    return 0


def main(filename):
    with open(filename, 'r') as file:
        towels = get_towels(file.readline().rstrip('\n'))
        file.readline()
        # print(towels)

        sum = 0
        # pdb.set_trace()
        for pattern in file.readlines():
            sum += can_arrange(pattern.rstrip('\n'), towels)
        print(sum)


main("input.small")
main("input")
