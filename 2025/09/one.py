def solve1(file):
    get_point = lambda expr: tuple(map(int, expr.split(',')))
    with open(file, 'r') as f:
        points = [ get_point(expr.strip()) for expr in f ]

    pairs = ( (p1, p2) for p1 in points for p2 in points if p1 < p2 )

    rectangle = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    # for p1, p2 in pairs: print(f"{p1=} {p2=} {rectangle(p1, p2)=}")
    return max((rectangle(p1, p2) for p1, p2 in pairs ))

from itertools import chain
def solve2(file):
    get_point = lambda expr: tuple(map(int, expr.split(',')))
    rectangle = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    with open(file, 'r') as f:
        red = tuple( get_point(expr.strip()) for expr in f )
    pairs = sorted([ (rectangle(p1, p2), p1, p2) for p1 in red for p2 in red if p1 < p2 ], reverse=True)

    xs_ = sorted(set(map(lambda el: el[0], red)))
    ys_ = sorted(set(map(lambda el: el[1], red)))
    xs = { val: i for i, val in enumerate(xs_) }
    ys = { val: i for i, val in enumerate(ys_) }
    # print(xs)
    # print(ys)

    field = [ [ '.' for _ in xs ] for _ in ys ]
    # print_field = lambda : print("\n".join("".join(col for col in row) for row in field), end="\n\n")

    def connect(p1, p2):
        x1_, y1_ = p1
        x2_, y2_ = p2
        x1, y1 = xs[x1_], ys[y1_]
        x2, y2 = xs[x2_], ys[y2_]

        for x,y in ((x,y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
        ):
            # print(f"\t{x=}{y=}")
            field[y][x] = "#"

    for i in range(1, len(red)):
        p1, p2 = red[i - 1], red[i]
        connect(p1, p2)

    connect(red[0], red[-1])

    perimeter = chain(
        ((x, 0) for x in range(0, len(xs))),
        ((x, len(ys) - 1) for x in range(0, len(xs))),
        ((0, y) for y in range(0, len(ys))),
        ((len(xs) - 1, y) for y in range(0, len(ys))),
    )


    for x, y in perimeter:
        if field[y][x] == '.':
            field[y][x] = ' '

    update = True
    while update:
        update = False
        for y in range(len(field[0])):
            for x in range(len(field)):
                if field[y][x] != ".": continue

                if any((field[y_][x_] == ' ' for x_, y_ in ((x-1, y), (x, y+1), (x+1,y) , (x, y+1)))):
                    field[y][x] = ' '
                    update = True

    for y in range(len(field[0])):
        for x in range(len(field)):
            if field[y][x] == '.':
                field[y][x] = "#"


    def in_field(p1, p2) -> bool:
        x1_, y1_ = p1
        x2_, y2_ = p2
        x1, y1 = xs[x1_], ys[y1_]
        x2, y2 = xs[x2_], ys[y2_]

        return all((field[y][x] == "#"
            for x,y in ((x,y)
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
            )
        ))

    for size, p1, p2 in pairs:
        if in_field(p1, p2):
            return size


print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
