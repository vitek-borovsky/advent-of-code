# import pdb

class Record:
    value: str
    size: int

    def __init__(self, value, size):
        self.value = value
        self.size = size

    def __repr__(self) -> str:
        return f"Record({self.value}, {self.size})"

    def copy(self):
        return Record(self.value, self.size)


def expand(file) -> list[Record]:
    inp: str = file.readline().rstrip('\n')
    result = []

    is_free = False
    id = 0
    for c in inp:
        n = int(c)
        if is_free:
            result.append(Record(".", n))
        else:
            result.append(Record(f"{id}", n))
            id += 1
        is_free = not is_free

    return result

def swap(l, i1, i2):
    t = l[i1]
    l[i1] = l[i2]
    l[i2] = t


def transform(expanded: list[Record]):
    left = 0
    right = len(expanded) - 1
    last_print = 0

    while 0 <= right:

        if left >= right:
            left = 0
            right -= 1
            continue

        if expanded[left].value != ".":
            left += 1
            continue

        if right % 1000 == 0 and last_print != right:
            last_print = right
            print(f"Right is now { right }")
        if expanded[right].value == ".":
            right -= 1
            continue

        if expanded[left].size < expanded[right].size:
            left += 1
            continue

        new_l = build_new_l(expanded, left, right)
        expanded = new_l
        left = 0
    return expanded

def s(start, size):
    sum = 0
    for i in range(start, start + size):
        sum += i
    return sum

def build_new_l(expanded, left, right):
        new_l = []
        for i in range(left):
            new_l.append(expanded[i].copy())

        new_l.append(Record(expanded[right].value, expanded[right].size))
        new_l.append(Record(".", expanded[left].size - expanded[right].size))
        expanded[right].value = "."

        for i in range(left + 1, len(expanded)):
            new_l.append(expanded[i].copy())
        return new_l

def pretty_print(l):
    s = ""
    for entry in l:
        s += f"{entry.value}" * entry.size

    print(s)



def calculate_checksum(expanded: list[Record]):
    sum = 0
    new_possition = 0
    possition = 0
    for entry in expanded:
        possition = new_possition
        new_possition += entry.size
        if entry.value == ".":
            continue

        sum += int(entry.value) * s(possition, entry.size)

    return sum

def main(file_name):
    with open(file_name, 'r') as file:
        expanded = expand(file)

    # pretty_print(expanded)
    expanded = transform(expanded)
    # pretty_print(expanded)
    return calculate_checksum(expanded)

print(f"SMALL: { main('input.small.txt') }")
print(f"FULL: { main('input.txt') }")
