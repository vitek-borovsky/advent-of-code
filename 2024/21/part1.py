from itertools import permutations
from itertools import product
from functools import cache
import pdb
NUMPAD = [
    [ "7", "8", "9", ],
    [ "4", "5", "6" ],
    [ "1", "2", "3" ],
    [ "@", "0", "A" ]
]
NUMPAD_KEYS = [ str(k) for k in list(range(10)) + [ "A" ] ]

DIRPAD = [
    [ "@", "^", "A" ],
    [ "<", "v", ">" ]
]
DIRPAD_KEYS = [ "^", "A", "<", "v", ">" ]

def is_valid(keypad, pos, sol):
    for dir in sol:
        if dir == ">": pos[0] += 1
        if dir == "<": pos[0] -= 1
        if dir == "v": pos[1] += 1
        if dir == "^": pos[1] -= 1

        if keypad[pos[1]][pos[0]] == "@":
            return False
    return True


def solve(keypad, KEYS):
    positions = { keypad[y][x]: (x,y) for x in range(len(keypad[0])) for y in range(len(keypad)) }
    paths: dict[tuple[str, str], list[str]] = {}

    for s in KEYS:
        for e in KEYS:
            sx, sy = positions[s]
            ex, ey = positions[e]
            p = ""
            if sx - ex < 0: p += ">" * abs(sx - ex)
            if ex - sx < 0: p += "<" * abs(sx - ex)
            if sy - ey < 0: p += "v" * abs(sy - ey)
            if ey - sy < 0: p += "^" * abs(sy - ey)

            res = { ''.join(p) for p in permutations(p) }
            paths[(s, e)] = list(res)

    # remove @ paths
    for s in KEYS:
        for e in KEYS:
            sol_new = []
            for sol in paths[(s,e)]:
                pos = [positions[s][0], positions[s][1]]
                if is_valid(keypad, pos, sol):
                    sol_new.append(sol)
            paths[(s,e)] = sol_new


    for s in KEYS:
        for e in KEYS:
            sol_new = []
            for sol in paths[(s,e)]:
                sol_new.append(sol + "A")
            paths[(s,e)] = sol_new

    return paths

def get_possibilities(inp: str, paths):
    steps = []
    for s,e in zip("A" + inp, inp):
        ps = paths[(s,e)]
        steps.append(ps)

    res = [ ''.join(sol) for sol in product(*steps) ]
    return res

def encode(r_inp_list: list[str], dirpad_paths, level=0):
    if level == 0: return r_inp_list

    r_inp_list_encoded = encode(r_inp_list, dirpad_paths, level - 1)
    r_new_list = []
    for r_inp in r_inp_list_encoded:
        r_new_list += get_possibilities(r_inp, dirpad_paths)

    minlen = min(map(len, r_new_list))
    r_new_list = [ s for s in r_new_list if len(s) == minlen ]

    return r_new_list



CODES = [ "382A", "176A", "463A", "083A", "789A" ]

numpad_paths = solve(NUMPAD, NUMPAD_KEYS)
dirpad_paths = solve(DIRPAD, DIRPAD_KEYS)

sum = 0
for code in CODES:
    # pdb.set_trace()
    r_start = get_possibilities(code, numpad_paths)

    r_final = encode(r_start, dirpad_paths, 2)
    sum +=  int(code.rstrip("A")) * len(r_final[0])
    print(len(r_final[0]))

print(sum)

