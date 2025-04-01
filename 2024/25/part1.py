import sys
import pdb

def process(key_lock, mp, C):
    res = [ 0 ] * 5
    for line in key_lock.split('\n'):
        for i,c in enumerate(line):
            if c == C: res[i] += 1

    res = tuple( i - 1 for i in res )
    if res not in mp: mp[res] = 0
    mp[res] += 1

def fits(key: tuple[int], lock: tuple[int]):
    # pdb.set_trace()
    for k, l in zip(key, lock):
        if k < l: return False
    return True


filename = sys.argv[1]

key_locks = open(filename).read().split('\n\n')

keys = {}
locks = {}
for key_lock in key_locks:
    is_lock = key_lock[0][0] == "#"
    if is_lock: process(key_lock, locks, "#")
    else: process(key_lock, keys, ".")


sm = sum(( keys[key] * locks[lock] for key in keys for lock in locks if fits(key,lock) ))

# print(locks)
# print(keys)
print(sm)
