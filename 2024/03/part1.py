import re

REGEX = r"mul\((\d{1,3})\,(\d{1,3})\)"


def match_string(input):
    matches = re.findall(REGEX, input)

    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
    return sum


with open("input.txt", 'r') as file:
    input = file.readlines()

input = "".join(input)

sum = 0
for part in input.split("do()"):
    working_part = part.split("don't()")[0]
    sum += match_string(working_part)

print(sum)

