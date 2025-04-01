

# WIDTH = 11
# HEIGHT = 7
WIDTH = 101
HEIGHT = 103
TIMES = 100
MID_X = (WIDTH - 1) / 2
MID_Y = (HEIGHT - 1) / 2

def move(point, vector, times):
    return (point[0] + vector[0] * times) % WIDTH, \
           (point[1] + vector[1] * times) % HEIGHT


def passline(line):
    p_l, p_v = line.split(' ')

    p_coor = p_l.split('=')[1].split(',')
    v_coor = p_v.split('=')[1].split(',')

    p = (int(p_coor[0]), int(p_coor[1]))
    v = (int(v_coor[0]), int(v_coor[1]))

    return p,v

def assign_quadrant(quadrants, point):
    if point[0] == MID_X:
        return

    if point[1] == MID_Y:
        return

    inx_x = int(point[0] > MID_X)
    inx_y = int(point[1] > MID_Y)

    quadrants[inx_y][inx_x] += 1

def print_drones(drones):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x,y) in drones: print("*", end = "")
            else: print(" ", end = "")
        print("")



def main(filename):
    min_list = []
    iter = 0
    drones: list[tuple[int,int]] = []
    vecs = []
    with open(filename, 'r') as file:
        for line in [ l.rstrip('\n') for l in file.readlines() ]:
            p,v = passline(line)
            drones.append(p)
            vecs.append(v)

    mn = float("inf")
    for _ in range(1, WIDTH * HEIGHT + 1):
        q = [[ 0, 0 ], \
             [ 0, 0 ]]
        for i in range(len(drones)):
            drones[i] = move(drones[i], vecs[i], 1)
            assign_quadrant(q, drones[i])

        sf = q[0][0] * \
             q[1][0] * \
             q[0][1] * \
             q[1][1]

        if sf < mn:
            mn = sf
            min_list = drones[:]
            iter = _


    print_drones({ d for d in min_list })
    print(iter)




# main('input.txt.small')
main('input.txt')
