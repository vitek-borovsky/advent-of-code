
def solve1(file):
    cur_val = 50

    with open(file, 'r') as f:
        answ = 0
        for line in f:
            if cur_val == 0:
                answ += 1

            line = line.strip()
            dir = line[0]
            val = int(line[1:])

            if dir == 'L': cur_val -= val
            else: cur_val += val

            cur_val %= 100

# print(f"{cur_val=}")
    print(f"solve1 {file=}: {answ=}")

def solve2(file):
    cur_val = 50

    with open(file, 'r') as f:
        answ = 0
        for line in f:
            line = line.strip()
            dir = line[0]
            val = int(line[1:])
            answ += val // 100
            val = val % 100

            prev_val = cur_val
            if dir == 'L': cur_val -= val
            else: cur_val += val

            old_val = cur_val
            cur_val %= 100

            if (old_val != cur_val or cur_val == 0) and prev_val != 0:
                answ += 1

    print(f"solve2 {file=}: {answ=}")

solve1("in.small")
solve1("in")

solve2("in.small")
solve2("in")
