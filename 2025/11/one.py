from functools import cache
def solve1(file):
    with open(file, 'r') as f:
        d = {
            left: tuple(r for r in right.split(' '))
            for left, right in (
                line.strip().split(': ')
                for line in f
            )
        }

    @cache
    def execute(source: str) -> int:
        if source == "out":
            return 1

        return sum((execute(out) for out in d[source]))

    return execute("you")

#############################################################
def solve2(file):
    with open(file, 'r') as f:
        d = {
            left: tuple(r for r in right.split(' '))
            for left, right in (
                line.strip().split(': ')
                for line in f
            )
        }


    #                                 N    DAC FFT   DAC&FFT
    @cache
    def execute(source: str) -> tuple[int, int, int, int]:
        if source == "out":
            return (1, 0, 0, 0)

        def prep():
            for out in d[source]:
                # print(f"{execute(out)=}")
                for i in range(4):
                    ex = execute(out)
                    # print(f"{out=} {ex=}")
                    ex[i]
            res = tuple(
                sum((execute(out)[i] for out in d[source]))
                for i in range(4)
            )
            return res

        p = prep()
        if source == "dac": return (0, p[0] + p[1], 0, p[2] + p[3])
        if source == "fft":  return (0, 0, p[0] + p[2], p[1] + p[3])

        return p

    return execute("svr")[3]


# print(solve1("in.small"))
# print(solve1("in"))

print(solve2("in.small2"))
print(solve2("in"))
