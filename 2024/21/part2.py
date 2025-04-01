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
    minlen = min(map(len, res))
    res = [ s for s in res if len(s) == minlen ]
    return res

@cache
def calculate_length(x: str, y: str, level) -> int:
    if level == 1: return len(dirpad_paths[(x,y)][0])

    min_len = float("inf")
    for path in dirpad_paths[(x,y)]:
        ln = 0
        for s,e in zip("A" + path, path):
            ln += calculate_length(s, e, level - 1)

        min_len = min(min_len, ln)
    return int(min_len)

CODES = [ "382A", "176A", "463A", "083A", "789A" ]

numpad_paths = solve(NUMPAD, NUMPAD_KEYS)
dirpad_paths = solve(DIRPAD, DIRPAD_KEYS)

sum = 0
for code in CODES:
    # pdb.set_trace()
    r_start = get_possibilities(code, numpad_paths)

    min_len = float("inf")
    for path in r_start:
        ln = 0
        for s,e in zip("A" + path, path):
            ln += calculate_length(s, e, 25)

        min_len = min(min_len, ln)

    print(min_len)
    sum += int(min_len) * int(code.rstrip("A"))


print(sum)

