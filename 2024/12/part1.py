class Region:
    tiles: set[tuple[int,int]]

    def __init__(self) -> None:
        self.circum = 0
        self.tiles = set()

    def add_tile(self, point):
        self.tiles.add(point)

    def get_area(self):
        return len(self.tiles)

    def max(self):
        max_x = 0
        max_y = 0
        for x,y in self.tiles:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return max_x, max_y


    def sort(self):
        sorted_x = list(self.tiles)
        sorted_y = [ (y,x) for x,y in sorted_x ]
        sorted_x.sort()
        sorted_y.sort()
        return sorted_x, sorted_y


    def get_circum(self):
        # max_x, max_y = self.max()
        # sorted_x, sorted_y = self.sort()
        return 0

def is_in_map(lines, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 not in range(0, len(lines[0])) or y1 not in range(0, len(lines)):
        return False

    if x2 not in range(0, len(lines[0])) or y2 not in range(0, len(lines)):
        return False
    return True


def is_same_idf(lines, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if not is_in_map(lines, p1, p2):
        return False

    return lines[y1][x1] == lines[y2][x2]

def bfs(lines, region, point, processed):
    if point in processed:
        return
    processed.add(point)
    region.add_tile(point)

    x, y = point
    if is_same_idf(lines, (x, y), (x-1, y)):
        bfs(lines, region, (x-1, y), processed)
    if is_same_idf(lines, (x, y), (x+1, y)):
        bfs(lines, region, (x+1, y), processed)
    if is_same_idf(lines, (x, y), (x, y-1)):
        bfs(lines, region, (x, y-1), processed)
    if is_same_idf(lines, (x, y), (x, y+1)):
        bfs(lines, region, (x, y+1), processed)


def main(file_name):
    processed = set()
    regions: list[Region] = []
    with open(file_name, 'r') as file:
        lines = [ line.rstrip('\n') for line in file.readlines() ]

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) not in processed:
                region = Region()
                bfs(lines, region, (x,y), processed)
                regions.append(region)

    # reg = list(regions)[1]
    # print(reg.get_area() * reg.get_circum())
    for reg in regions:
        print(reg.get_circum(), end=": ")
        print(reg.get_area() * reg.get_circum())

    return sum(( reg.get_area() * reg.get_circum() for reg in regions))


print(f"SMALL: { main('input.small.txt') }")
# print(f"FULL: { main('input.txt') }")
