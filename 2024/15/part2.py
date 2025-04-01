def load_input(lines: list[str]):
    for i in range(len(lines)):
        if lines[i] == "\n":
            map = lines[:i]

            movement = lines[i:]
            map = [
                list(
                    l
                    .rstrip('\n')
                    .replace(".", "..")
                    .replace("@", "@.")
                    .replace("O", "[]")
                    .replace("#","##")
                ) for l in map ]

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

def is_movable(map, move_vec, space, rec = True):
    val = map[space[1]][space[0]]
    if val == "@":
        return is_movable(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
    if val == ".":
        return True
    if val == "#":
        return False
    if val == "[":
        if not rec or move_vec[0] != 0:
            return is_movable(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
        else:
            return is_movable(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1])) \
               and is_movable(map, move_vec, (space[0] + 1, space[1]), False)

    if val == "]":
        if not rec or move_vec[0] != 0:
            return is_movable(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
        else:
            return is_movable(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1])) \
               and is_movable(map, move_vec, (space[0] - 1, space[1]), False)
    print("ERROR")


def move_rob(map, move_vec, space, rec = True):
    val = map[space[1]][space[0]]
    if val == "@":
        move_rob(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))

    if val == ".":
        return

    if val == "#":
        print("ERROR, MOVING, WALL")

    if val == "[":
        if not rec or move_vec[0] != 0:
            move_rob(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
        else:
            move_rob(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
            move_rob(map, move_vec, (space[0] + 1, space[1]), False)

    if val == "]":
        if not rec or move_vec[0] != 0:
            move_rob(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
        else:
            move_rob(map, move_vec, (space[0] + move_vec[0], space[1] + move_vec[1]))
            move_rob(map, move_vec, (space[0] - 1, space[1]), False)

    map[space[1] + move_vec[1]][space[0] + move_vec[0]] = map[space[1]][space[0]]
    map[space[1]][space[0]] = "."

def make_move(map, move, robot):
    # print(move, end=": ")
    move_vec = decode_move_vector(move)
    if is_movable(map, move_vec, robot):
        move_rob(map, move_vec, robot)
        robot[0] += move_vec[0]
        robot[1] += move_vec[1]
        return


def calculate_GPS(map):
    sum = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "[":
                sum += 100 * y + x
    return sum


def main(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        map, movement = load_input(lines)

    # print("\n".join([ "".join(l) for l in map ]))
    # input()
    robot = find_robot(map)
    for move in movement:
        # print(f"moving {move}")
        make_move(map, move, robot)
        # print("\n".join([ "".join(l) for l in map ]))
        # input()


    print(calculate_GPS(map))

main("input.small")
main("input.small.2")
main("input")
