# import pdb

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

class Record:
    p: Point
    facing: list

    def __init__(self, p, facing) -> None:
        self.p = p
        self.facing = facing

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.p == other.p and self.facing[0] == other.facing[0] and self.facing[1] == other.facing[1]
        return False

    def __hash__(self) -> int:
        return hash((self.p, self.facing[0], self.facing[1]))

LEFT = [ -1, 0 ]
RIGHT = [ 1, 0 ]
UP = [ 0, -1 ]
DOWN = [ 0, 1 ]

def rotate_right(facing) -> list:
    global LEFT, RIGHT, UP, DOWN
    if facing == LEFT:
        return UP

    if facing == UP:
        return RIGHT

    if facing == RIGHT:
        return DOWN

    if facing == DOWN:
        return LEFT

    return []


def decode_facing(facing):
    if facing == LEFT:
        return "LEFT"

    if facing == UP:
        return "UP"

    if facing == RIGHT:
        return "RIGHT"

    if facing == DOWN:
        return "DOWN"



walls: set[Point] = set()
starting_possiton: Point = Point(0,0)
facing = UP
MAX_X: int = 0
MAX_Y: int = 0


def load_input(file):
    global walls, starting_possiton, MAX_X, MAX_Y
    for y, line in enumerate(file.readlines()):
        for x, c in enumerate(line.strip('\n')):
            if c == "#":
                walls.add(Point(x,y))
            if c == "^":
                starting_possiton = Point(x,y)
            MAX_X = x + 1
            MAX_Y = y + 1

def get_next_position(curr_position, facing):
    return Point(curr_position.x + facing[0], curr_position.y + facing[1])

def is_in_map(possition):
    global MAX_X, MAX_Y
    return possition.x >= 0 and possition.x < MAX_X \
       and possition.y >= 0 and possition.y < MAX_Y


def simulate(current_positon, facing: list, walls):
    """False = we got out of map"""
    # visited: set[Point] = set()
    # visited.add(starting_possiton)

    visited_plus: set[ Record ] = set()


    while True:
        next_pos = get_next_position(current_positon, facing)
        if (not is_in_map(next_pos)):
            return False

        if next_pos in walls:
            facing = rotate_right(facing)
            continue

        # print(f"Moving [{ decode_facing(facing) }] { current_positon } -> { next_pos }")
        # visited.add(next_pos)
        new_record = Record(next_pos, facing[:])
        if new_record in visited_plus:
            return True
        visited_plus.add(new_record)
        current_positon = next_pos


    # return len(visited)

# with open("input.small.txt", 'r') as file:
with open("input.txt", 'r') as file:
    load_input(file)

sum = 0
for x in range(MAX_X):
    print(f"Starting { x }")
    for y in range(MAX_Y):
        if Point(x,y) in walls:
            continue
        current_positon = starting_possiton
        facing = UP
        new_walls = walls.copy()
        new_walls.add(Point(x,y))
        if (simulate(current_positon, facing, new_walls)):
            sum += 1

print(sum)
# print(simulate(current_positon, facing, walls))



