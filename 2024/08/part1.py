# import pdb
from itertools import combinations

class Point:
    x: int
    y: int
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))  # Hash based on the coordinates

    def __repr__(self) -> str:
        return f"Point({ self.x }, { self.y })"

def load_data(file):
    global height, width
    antenas: dict[str, set[Point]] = { }
    data = file.readlines()
    data = [ line.rstrip('\n') for line in data ]
    for y in range(len(data)):
        for x in range(len(data[y])):
            height = y + 1
            width = x + 1
            c = data[y][x]
            if c == '.' or c == '#':
                continue
            if c not in antenas:
                antenas[c] = set()
            antenas[c].add(Point(x, y))
    return antenas

def calculate_antinodes(antenas: set[Point]) -> set[Point]:
    result = set()
    for a1, a2 in combinations(antenas, 2):
        result = result.union(calculate_anitodes_from_two(a1, a2))
    return result

def distance(p1, p2) -> int:
    return (abs(p1.x - p2.x) ** 2) + (abs(p1.y - p2.y) ** 2)

def calculate_anitodes_from_two(antenna1, antenna2) -> set[Point]:
    global height, width
    v = (antenna1.x - antenna2.x, antenna1.y - antenna2.y)
    v_rev = (antenna2.x - antenna1.x, antenna2.y - antenna1.y)


    s1 = { Point(antenna1.x + n * v[0], antenna1.y + n * v[1]) for n in range(max(height, width)) }
    s2 = { Point(antenna2.x + n * v_rev[0], antenna2.y + n * v_rev[1]) for n in range(max(height, width)) }

    return s1.union(s2)


def is_point_in_field(point):
    global height, width
    return 0 <= point.x and point.x < width \
       and 0 <= point.y and point.y < height


height = 0
width = 0

# height = 5
# width = 5
# p1 = Point(2,2)
# p2 = Point(3,3)
# print(calculate_anitodes_from_two(p1, p2))


def main(file_name):
    with open(file_name, 'r') as file:
        antenas = load_data(file)

    antinodes: set[Point] = set()
    for key in antenas:
        antinodes = antinodes.union(calculate_antinodes(antenas[key]))

    # filter those in field
    antinodes = { point  \
         for point in antinodes \
         if is_point_in_field(point) \
    }

    return len(antinodes)

print(f"SMALL: { main('input.small.txt') }")
print(f"FULL: { main('input.txt') }")

