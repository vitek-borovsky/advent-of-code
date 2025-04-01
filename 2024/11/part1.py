from functools import lru_cache

def manual_transform(stone: int) -> list[int]:
    if stone == 0:
        return [ 1 ]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        len_h = len(s) // 2
        i1: int = int(s[:len_h])
        i2: int = int(s[len_h:])
        return [ i1, i2]
    else:
        return [ stone * 2024 ]

DP = {}
def blink(stone: int, times: int) -> int:
    if (stone, times) in DP:
        return DP[(stone, times)]
    if times == 0:
        return 1

    res = sum(( blink(st, times - 1) for st in manual_transform(stone) ))
    DP[(stone, times)] = res
    return res


def main(file_name):
    with open(file_name, 'r') as file:
        stones = [ int(s) for s in file.readline().strip('\n').split(' ') ]

    return sum (( blink(stone, 75) for stone in stones ))


print(f"SMALL: { main('input.small.txt') }")
print(f"FULL: { main('input.txt') }")
