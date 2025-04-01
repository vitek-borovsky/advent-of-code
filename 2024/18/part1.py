from queue import PriorityQueue
import pdb

def load_input(lines):
    lines = [ l.rstrip('\n') for l in lines ]

    w,h = lines[0].split(',')
    WIDTH, HEIGHT = int(w), int(h)

    walls = set()
    for rec in lines[2:]:
        if rec == '':
            break
        x,y = rec.split(',')
        walls.add((int(x), int(y)))

    map = [ [ "." for _ in range(WIDTH) ] for _ in range(HEIGHT) ]
    map[HEIGHT - 1][WIDTH - 1] = "E"
    for x,y in walls:
        map[y][x] = "#"

    return WIDTH, HEIGHT, map

def get(map, x, y, WIDTH, HEIGHT):
    if not x in range(0, WIDTH):
        return "#"

    if not y in range(0, HEIGHT):
        return "#"

    return map[y][x]

MIN_END = -1

def bfs(q: PriorityQueue[tuple[int, tuple[int,int]]], WIDTH, HEIGHT, map):
    print("\n".join([ "".join(l) for l in map]))
    processed = set()
    while not q.empty():
        prio, coor = q.get()
        x,y = coor
        if (x,y) in processed:
            continue
        processed.add( (x,y) )
        bfs_step(q, prio, x, y, WIDTH, HEIGHT, map)


def bfs_step(q,prio, x, y, WIDTH, HEIGHT, map):
    # print(f"Seaching ({x}, {y})")
    global MIN_END
    if MIN_END != -1:
        return

    val = get(map, x, y, WIDTH, HEIGHT)
    if val == "#": return
    if val == "E":
        MIN_END = prio
        return

    q.put( (prio + 1, (x + 1,y) ) )
    q.put( (prio + 1, (x - 1,y) ) )
    q.put( (prio + 1, (x,y + 1) ) )
    q.put( (prio + 1, (x,y - 1) ) )

def main(filename):
    global MIN_END
    MIN_END = -1
    with open(filename, 'r') as file:
        WIDTH, HEIGHT, map = load_input(file.readlines())

    # pdb.set_trace()

    q = PriorityQueue()
    q.put( (0, (0,0) ) )

    bfs(q, WIDTH, HEIGHT, map)
    print(MIN_END)

main("input")
