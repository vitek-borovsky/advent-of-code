# import pdb

def processline(line):
    sum, body = line.split(':')
    operands = body.strip(' ').strip('\n').split(' ')
    sum = int(sum)
    operands = [ int(o) for o in operands ]

    partial_results = { operands[ 0 ] }
    for operand in operands[1::]:
        new_partial_result = set()
        for pr in partial_results:
            new_partial_result.add(pr + operand)
            new_partial_result.add(pr * operand)
            new_partial_result.add(int(str(pr) + str(operand)))

        partial_results = new_partial_result

    if sum in partial_results:
        return sum
    return 0

result = 0
# with open("input.small.txt", 'r') as file:
with open("input.txt", 'r') as file:
    for line in file.readlines():
        result += processline(line)


print(result)
