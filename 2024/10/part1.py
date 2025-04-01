# import pdb

def load_map(file):
    map = []
    for line in file.readlines():
        line_map = []
        for c in line.rstrip('\n'):
            c = int(c)
            line_map.append(c)
        map.append(line_map)
    return map

def find_ends(map):
    return {
        (x, y) \
        for y in range(len(map)) \
            for x in range(len(map[0])) \
                if map[y][x] == 9 \
    }

def get_at(map, point):
    x, y = point
    if y < 0 or y >= len(map):
        return -1

    if x < 0 or x >= len(map[0]):
        return -1

    return map[y][x]



def search_imp(map: list[list[int]], ends: dict[tuple[int,int], int], curr_val) -> dict[tuple[int,int], int]:
    if curr_val == 0:
        return {} # TODO

    result: dict[tuple[int,int], int] = {}
    for point in ends:
        x, y = point
        searchpoints = { \
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        }

        for sp in searchpoints:
            if get_at(map, sp) == curr_val - 1:
                if sp not in result:
                    result[sp] = 0

                result[sp] += ends[(x,y)]

    return result

def search(map: list[list[int]], ends: set[tuple[int,int]]) -> int:
    new_ends: dict[tuple[int,int], int] = { e : 1 for e in ends }
    for curr_val in range(9, 0, -1):
        new_ends = search_imp(map, new_ends, curr_val)

    sum = 0
    for key in new_ends:
        sum += new_ends[key]

    return sum

def main(file_name):
    with open(file_name, 'r') as file:
        map = load_map(file)

    ends = find_ends(map)
    return search(map, ends)
    # print(map)
    # print(heads)






    return 0

print(f"SMALL: { main('input.small.txt') }")
print(f"FULL: { main('input.txt') }")
