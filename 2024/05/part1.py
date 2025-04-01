# import pdb
import itertools
from functools import cmp_to_key

def popululate_before(file):
    while True:
        line = file.readline().rstrip('\n')
        if line == "":
            break

        bef, aft = line.split('|')
        bef = int(bef)
        aft = int(aft)

        if bef not in before:
            before[bef] = set()

        before[bef].add(aft)

def check_update_validity(page_numbers):
    seen_pages = set()
    for page_no in page_numbers:
        if page_no in before \
            and seen_pages.intersection(before[page_no]) != set():
            return False

        seen_pages.add(page_no)
    return True

def get_middle(page_numbers) -> int:
    return page_numbers[len(page_numbers) // 2]


def get_correct_permutation(page_numbers):
    for permutation in itertools.permutations(page_numbers):
        if (check_update_validity(permutation)):
            return permutation


def my_comp(x, y):
    if x in before and y in before[x]:
        return 1

    if y in before and x in before[y]:
        return -1

    return 1 if x < y else -1


sum = 0
before : dict[ int, set[int] ] = { }
# with open("input.small.txt", 'r') as file:
with open("input.txt", 'r') as file:
    popululate_before(file)
    for update in file.readlines():
        page_numbers = update.rstrip('\n').split(",")
        page_numbers = [ int(n) for n in page_numbers ]

        if check_update_validity(page_numbers):
            continue

        # print(page_numbers)
        page_numbers.sort(key = cmp_to_key(my_comp))
        # print(page_numbers)
        # print("")
        sum += get_middle(page_numbers)




print(sum)

