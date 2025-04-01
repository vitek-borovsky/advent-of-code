from queue import Queue
import pdb
INF = 999999999999999999999999

def read_map(lines) -> list[list[str]]:
    lines = [ list(line.rstrip('\n')) for line in lines ]
    return lines

def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                return x,y
    print("ERROR, NOSTART")
    return -1, -1

def get(map, x, y):
    if not x in range(0, len(map[0])):
        return "#"

    if not y in range(0, len(map)):
        return "#"

    return map[y][x]


neighbours = {
    ( -1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
}

def mark(map):
    arr = [(-1, -1) for _ in range(100000) ]
    q = Queue()
    sx, sy = find_start(map)
    q.put( (0, (sx, sy)) )

    while not q.empty():
        cnt, coor = q.get()
        x, y = coor
        mark_impl(map, x, y, cnt, arr, q)

    while arr[-1] == (-1, -1):
        arr.pop()
    return arr

def mark_impl(map, sx, sy, cnt, arr, q):
    if get(map, sx, sy) == "#":
        return

    if get(map, sx, sy) in "SE.":
        map[sy][sx] = "-"
        arr[cnt] = (sy, sx)
        for x, y in neighbours:
            q.put( (cnt + 1, (sx + x, sy + y) ) )


def distance(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_cheats(arr, threshhold):
    res = 0
    for i in range(len(arr)):
        if i % 1000 == 0:
            print(f"{i} out of {len(arr)}")

        for j in range(i + threshhold, len(arr)):
            dist = distance(arr[i], arr[j])
            if dist > 20:
                continue
            shortcut = (j - i) - dist
            if shortcut >= threshhold:
                res += 1

    return res

def main(filename, threshhold):
    print("LOADING")
    with open(filename, 'r') as file:
        map = read_map(file.readlines())
    print("MARKING")
    arr = mark(map)
    # pdb.set_trace()
    print("CALCULATING CHEATS")
    cheats = calculate_cheats(arr, threshhold)
    print(cheats)

main("input.small", 50) # 285
main("input", 100)
