import pdb

# B = A % 8           (B in [0, 7])
# B = B ^ 1           (B in [0, 7])
# C = A / (2 ** B)    (C = A >> B)
# B = B ^ 0b101       (B in [0, 7])
# B = B ^ C           (B ~ C)
# OUT B % 8           ()
# A = B / (2 ** 3)    (A = B >> 3)
# if A != 0 jmp 0     ()

def perform_round_inv(PROGRAM, part_ans):
    print(PROGRAM, part_ans)
    if PROGRAM == []: return part_ans
    for b in range(8):
        A = part_ans << 3 | b
        B = A % 8
        B ^= 1
        C = A >> B
        B ^= 5
        B ^= C
        if B % 8 == PROGRAM[-1]:
            sol = perform_round_inv(PROGRAM[:-1], A)
            if sol is None: continue
            return sol


PROGRAM = [2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0]

PROGRAM = [0,3,5,4,3,0]
print(perform_round_inv(PROGRAM, 0))
