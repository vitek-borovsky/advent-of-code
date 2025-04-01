from queue import PriorityQueue


def read_map(lines) -> tuple[str]:
    lines = tuple( line.rstrip('\n') for line in lines )
    return lines

def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                return x,y
    print("ERROR, NOSTART")
    return -1, -1

"""
    PriorityQueue(
        (
            priority
            (
                x
                y
                (
                    facing_x
                    facing_y
                )
            )
        )
    )
"""
def search(map, pq: PriorityQueue[tuple[int, tuple[int, int, tuple[int,int]]]]):
    while True:
        prio, coor = pq.get()
        x, y, facing = coor
        if map[y][x] == "E":
            return prio

        if map[y][x] == "#":
            continue

        search_one(map, pq, x, y, facing, prio)

def rotate_left(coor):
    return (coor[1], coor[0])

def rotate_right(coor):
    return (-coor[1], -coor[0])

DP = set()
def search_one(map, pq: PriorityQueue[tuple[int, tuple[int, int, tuple[int,int]]]], x, y, facing, priority_curr):
    if (x, y, facing) in DP:
        return
    DP.add((x,y,facing))

    # print(f"searching ({x}, {y}) @ {priority_curr}")
    fac_x, fac_y = facing
    pq.put((priority_curr + 1, (x + fac_x, y + fac_y, (fac_x, fac_y))))
    pq.put((priority_curr + 1000, (x, y, rotate_left((fac_x, fac_y)))))
    pq.put((priority_curr + 1000, (x, y, rotate_right((fac_x, fac_y)))))

def main(filename):
    global DP
    DP = set()
    with open(filename, 'r') as file:
        map = read_map(file.readlines())
    sx, sy = find_start(map)
    pq = PriorityQueue()
    pq.put( (0, (sx, sy, (1, 0)) ) )

    res = search(map, pq)
    print(res)


main("input.small")
main("input.small2")
main("input")
