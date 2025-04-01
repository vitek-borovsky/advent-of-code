def get_at_inx(input, x, y):
    if (x < 0 or len(input[0]) <= x):
        return '.'

    if (y < 0 or len(input) <= y):
        return '.'

    return input[y][x]

def test_possition(input, x, y):
    if get_at_inx(input, x, y) != 'A':
        return False

    s1 = { get_at_inx(input, x - 1, y - 1), get_at_inx(input, x + 1, y + 1) }
    s2 = { get_at_inx(input, x + 1, y - 1), get_at_inx(input, x - 1, y + 1) }

    return 'M' in s1 and 'M' in s2 and 'S' in s1 and 'S' in s2


def search_with_vector(input):
    sum = 0

    for x in range(len(input[0])):
        for y in range(len(input)):
            if test_possition(input, x, y):
                sum += 1


    return sum


with open("input.txt", 'r') as file:
    input = file.readlines()

sum = 0

sum += search_with_vector(input);

print(sum)

