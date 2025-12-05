# I've extended the input files with help of editors
# I've added . around the input
def solve1(file):
    with open(file, 'r') as f:
        matrix_ = f.readlines()
        matrix = tuple( l.strip() for l in matrix_ )

    is_wall = lambda col, row: matrix[row][col] == "@"
    is_accesible = lambda col, row: \
        sum((
            is_wall(col - 1, row),
            is_wall(col - 1, row - 1),
            is_wall(col, row - 1),
            is_wall(col + 1, row - 1),
            is_wall(col + 1, row),
            is_wall(col + 1, row + 1),
            is_wall(col, row + 1),
            is_wall(col - 1, row + 1),
        )) < 4

    rows = len(matrix)
    cols = len(matrix[0])
    return sum((
        is_wall(col, row) and is_accesible(col, row)
        for col in range(1, cols - 1)
        for row in range(1, rows - 1)
    ))

def solve2(file):
    with open(file, 'r') as f:
        matrix_ = f.readlines()
        matrix = [ list(l.strip()) for l in matrix_ ]

    is_wall = lambda col, row: matrix[row][col] == "@"
    is_accesible = lambda col, row: \
        sum((
            is_wall(col - 1, row),
            is_wall(col - 1, row - 1),
            is_wall(col, row - 1),
            is_wall(col + 1, row - 1),
            is_wall(col + 1, row),
            is_wall(col + 1, row + 1),
            is_wall(col, row + 1),
            is_wall(col - 1, row + 1),
        )) < 4

    is_removable = lambda col, row: is_wall(col, row) and is_accesible(col, row)

    rows = len(matrix)
    cols = len(matrix[0])
    total = 0
    changed = True
    while changed:
        changed = False
        for col in range(1, cols - 1):
            for row in range(1, rows - 1):
                if is_removable(col, row):
                    changed = True
                    total += 1
                    matrix[row][col] = "."

    return total

print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
