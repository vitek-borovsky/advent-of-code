import pdb
def mix(n1, n2):
    return n1 ^ n2

def prune(n):
    return n % 16777216

def mix_and_prune(n1, n2):
    return prune(mix(n1,n2))

def get_next(n):
    n = mix_and_prune(n, n * 64)
    n = mix_and_prune(n, n // 32)
    n = mix_and_prune(n, n * 2048)
    return n

def get_change(n1, n2):
    return (n2 % 10) - (n1 % 10)

def push_changes(changes, new_val):
    changes[0] = changes[1]
    changes[1] = changes[2]
    changes[2] = changes[3]
    changes[3] = new_val

def process_seq(prices, changes, num):
    key = tuple(changes)
    if key in prices:
        return

    price = num % 10
    prices[key] = price


def process_num(num):
    S = 4
    changes = []
    prices = { }

    num = int(num)
    for _ in range(S):
        next_num = get_next(num)
        changes.append(get_change(num, next_num))
        num = next_num

    process_seq(prices, changes, num)

    for _ in range(2000 - S):
        next_num = get_next(num)
        push_changes(changes, get_change(num, next_num))
        num = next_num
        process_seq(prices, changes, num)

    return prices

def find_max(all_prices):
    mx = 0
    for a in range(-9, 10):
        print(f"A: {a}")
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    key = (a,b,c,d)
                    sum = 0
                    for prices in all_prices:
                        if key in prices:
                            sum += prices[key]
                    mx = max(mx, sum)
    return mx



def main(filename):
    lines = open(filename, 'r').read().splitlines()

    all_prices = []
    for num in lines:
        all_prices.append(process_num(num))

    mx = find_max(all_prices)
    print(mx)


# main("input.small")
main("input")

