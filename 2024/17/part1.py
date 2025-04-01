import pdb

A :int = 0
B: int = 0
C: int = 0
PROGRAM: list[int] = []
OUT: list[int] = []

def load_input(lines):
    global A,B,C,PROGRAM
    lines = [ l.rstrip('\n') for l in lines ]
    A_, B_, C_, PROGRAM_ = lines[0], lines[1], lines[2], lines[4]

    A = int(A_.split(':')[1])
    B = int(B_.split(':')[1])
    C = int(C_.split(':')[1])
    PROGRAM = [ int(inst) for inst in PROGRAM_.split(' ')[1].split(',') ]

def decode_combo(val) -> int:
    global A,B,C
    if val in [ 0, 1, 2, 3 ]:
        return val

    if val == 4:
        return A

    if val == 5:
        return B

    if val == 6:
        return C

    print(f"ERROR, DECODING COMBO, {val}")
    return -1

def process_instruction(inx: int):
    global A,B,C,PROGRAM,OUT
    opcode = PROGRAM[inx]
    # adv (combo)
    if opcode == 0:
        literal = decode_combo(PROGRAM[inx + 1])
        A = int(A // (2 ** literal ))
        return inx + 2

    # bxl (literal)
    if opcode == 1:
        literal = PROGRAM[inx + 1]
        B = B ^ literal
        return inx + 2

    # bst (combo)
    if opcode == 2:
        literal = decode_combo(PROGRAM[inx + 1])
        B = literal % 8
        return inx + 2

    # jnz (literal)
    if opcode == 3:
        if A == 0:
            return inx + 2
        literal = PROGRAM[inx + 1]
        return literal

    # bxc (B + C)
    if opcode == 4:
        B = B ^ C
        return inx + 2

    # out (combo)
    if opcode == 5:
        literal = decode_combo(PROGRAM[inx + 1])
        OUT.append(literal % 8)
        return inx + 2

    # bdv (combo)
    if opcode == 6:
        literal = decode_combo(PROGRAM[inx + 1])
        B = int(A // (2 ** literal ))
        return inx + 2

    # cdv (combo)
    if opcode == 7:
        literal = decode_combo(PROGRAM[inx + 1])
        C = int(A // (2 ** literal ))
        return inx + 2

    print(f"ERROR, INVALID_OPCODE {opcode}")
    return -1

def main(filename):
    global A,B,C,PROGRAM, OUT
    A = B = C = 0
    PROGRAM = []
    OUT = []
    with open(filename, 'r') as file:
        load_input(file.readlines())

    inx = 0
    while inx < len(PROGRAM):
        # print(f"INX: {inx}")
        # pdb.set_trace()
        inx = process_instruction(inx)

    OUT_ = [ str(e) for e in OUT ]
    print(",".join(OUT_))

main("input.small")
main("input")
