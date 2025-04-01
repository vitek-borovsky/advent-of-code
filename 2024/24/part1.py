from queue import Queue

def process_gate(op1, op2, gate) -> int:
    if gate == "AND":
        return op1 & op2

    if gate == "OR":
        return op1 | op2

    if gate == "XOR":
        return op1 ^ op2

    print("ERROR", gate)
    return -1

def build_result(z_values):
    result = 0
    for i in range(10):
        for j in range(10):
            key = f"z{i}{j}"
            if key not in z_values:
                return result

            val = z_values[key]
            result |= val << int(f"{i}{j}")

def main(filename, X, Y):
    lines = open(filename).read().splitlines()

    wire_values: dict[str, int] = {}
    X %= 2**46
    Y %= 2**46

    X_str = f"{X:b}"
    Y_str = f"{Y:b}"
    for i in range(45):
        name = f"x{i:02}"
        wire_values[name] = int(X_str[- i - 1])

    for i in range(45):
        name = f"y{i:02}"
        wire_values[name] = int(Y_str[- i - 1])

    sp = [ i for i in range(len(lines)) if lines[i] == '' ][0]
    # for line in lines[:sp]:
    #     name, val = line.split(':')
    #     wire_values[name] = int(val.lstrip())

    # (op1, op2, gate, result_op)
    swaps = {
        "qff": "qnw",
        "qnw": "qff",

        "qqp": "z23",
        "z23": "qqp",

        "fbq": "z36",
        "z36": "fbq",

        "pbv": "z16",
        "z16": "pbv",
    }


    q = Queue()
    for line in lines[sp + 1:]:
        op1, gate, op2, _, result_op = line.split(' ')
        if result_op in swaps:
            result_op = swaps[result_op]

        q.put((op1, op2, gate, result_op))

    while not q.empty():
        op1, op2, gate, result_op = q.get()
        if op1 not in wire_values.keys() or op2 not in wire_values.keys():
            q.put((op1, op2, gate, result_op))
            continue

        wire_values[result_op] = process_gate(wire_values[op1], wire_values[op2], gate)

    z_values = { key: wire_values[key] for key in wire_values.keys() if key[0] == 'z' }

    Z_RES = build_result(z_values)
    Z = X + Y
    print (f"{Z ^ Z_RES:b}")




# main("input.small")
main("input", 23242423432432432432432321329084329098, 239048238904902394803290840892091)
# 1000000000000000000000 00000 1111 0000 0000 0000 0000
