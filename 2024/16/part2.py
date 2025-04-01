from queue import PriorityQueue
import pdb

class State:
    def __init__(self, x, y, facing, callback = "NONE") -> None:
        self.x = x
        self.y = y
        self.facing = facing
        self.callback = callback

    def get_state_simp(self):
        return self.x, self.y, self.facing

    def get_callback(self):
        return self.callback

    def __lt__(self, other):
        return self.get_state_simp() < other.get_state_simp()

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

def find_end(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "E":
                return x,y
    print("ERROR, NOEND")
    return -1, -1

def rotate_left(coor):
    return (coor[1], coor[0])

def rotate_right(coor):
    return (-coor[1], -coor[0])

def search_one(pq, prio, state):
    global BEST_PATH
    if BEST_PATH != -1 and BEST_PATH < prio:
        return

    x,y,facing = state.get_state_simp()
    fac_x, fac_y = facing

    # print(f"searching ({x}, {y}) @ {prio}")
    pq.put((prio + 1, State(x + fac_x, y + fac_y, facing, state.get_state_simp())))
    pq.put((prio + 1000, State(x, y, rotate_left(facing), state.get_state_simp())))
    pq.put((prio + 1000, State(x, y, rotate_right(facing), state.get_state_simp())))

def search(map, pq: PriorityQueue[tuple[int, State]]):
    global BEST_PATH
    # (x,y, facing) -> min_prio
    DP = {}
    # (x,y, facing) -> set( (x,y,facing) )
    CALLBACKS = {}
    while not pq.empty():
        prio, state = pq.get()
        x, y, _ = state.get_state_simp()
        if map[y][x] == "#":
            continue

        if map[y][x] == "E":
            if BEST_PATH == -1:
                BEST_PATH = prio

        state_simp = state.get_state_simp()

        if state_simp not in DP:
            DP[state_simp] = prio
            CALLBACKS[state_simp] = { state.get_callback() }
        else:
            if DP[state_simp] == prio:
                CALLBACKS[state_simp].add(state.get_callback())
            continue

        search_one(pq, prio, state)

    # collect callbacks
    # pdb.set_trace()
    st = set()
    end_x, end_y = find_end(map)
    for dir in ( (-1,0), (1,0), (0,-1), (0,1) ):
        st.add((end_x, end_y, dir))

    while True:
        new_st = { r for r in st }
        for r in st:
            if r in CALLBACKS:
                new_st = new_st.union(CALLBACKS[r])
        if len(st) == len(new_st):
            break
        st = new_st

    # print(st, "\n")
    sanitized = { x for x in st if x != "NONE" }
    # print(sanitized, "\n")
    sanitized = { (x,y) for x,y,_ in sanitized }
    # print(sanitized, "\n")
    return len(sanitized)
    # return 0


BEST_PATH = -1
def main(filename):
    global BEST_PATH
    BEST_PATH = -1
    with open(filename, 'r') as file:
        map = read_map(file.readlines())
    sx, sy = find_start(map)
    pq = PriorityQueue()
    pq.put( (0, State(sx, sy, (1, 0)) ) )

    res = search(map, pq)
    print(res)


main("input.small")
main("input.small2")
main("input")
