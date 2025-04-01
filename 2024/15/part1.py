
def load_input(lines):
    for i in range(len(lines)):
        if lines[i] == "\n":
            map = lines[:i]
            movement = lines[i:]
            map = [ list(l.rstrip('\n')) for l in map ]
            movement = [ l.rstrip('\n') for l in movement ]
            return map, "".join(movement)
    print("ERROR, INPUT")
    return [], []

def find_robot(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "@":
                return [x,y]
    print("ERROR, FIND_ROBOT")
    return [-1, -1]


def decode_move_vector(move):
    if move == "^":
        return 0, -1
    if move == "v":
        return 0, 1
    if move == "<":
        return -1, 0
    if move == ">":
        return 1, 0

    print("ERROR, MOVE_VECTOR")
    return -1, -1

def make_move(map, move, robot):
    # print(move, end=": ")
    move_vec = decode_move_vector(move)
    for i in range(1, 1000):
        space = (robot[0] + i * move_vec[0], robot[1] + i * move_vec[1])
        val = map[space[1]][space[0]]
        if val == "#":
            # print("HIT A WALL")
            return
        if val == ".":
            # print("MOVING")
            map[robot[1]][robot[0]] = "."
            map[space[1]][space[0]] = "O"
            robot[0] += move_vec[0]
            robot[1] += move_vec[1]
            map[robot[1]][robot[0]] = "@"
            return
        if val == "O":
            # print("BOX-CONTINUING")
            continue
        print(f"ERROR, UNKNOWN CHAR IN MAP {val}")
        return

def calculate_GPS(map):
    sum = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "O":
                sum += 100 * y + x
    return sum


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        map, movement = load_input(lines)

    robot = find_robot(map)
    for move in movement:
        make_move(map, move, robot)

    print(calculate_GPS(map))

main("input.small")
main("input.small.2")
main("input")
