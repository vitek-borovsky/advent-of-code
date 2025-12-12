import re
LINE_RE = re.compile(
    r"""
    ^\[
        (?P<bracket>[.#]+)
    \]\s*
    (?P<parens>(?:\([0-9,]*\)\s*)+)
    \{
        (?P<braces>[0-9,]+)
    \}
    $
    """, re.VERBOSE
)
def parse_line(s: str) -> tuple[tuple[bool, ...], tuple[tuple[int, ...], ...], tuple[int, ...]] :
    m = LINE_RE.match(s)
    if not m: raise ValueError("Line does not match format")
    bracket_str = m.group("bracket")
    bracket_tup = tuple(c == '#' for c in bracket_str)

    paren_part = m.group("parens")
    paren_tuples = tuple(
        tuple(int(x) for x in group.split(",") if x)
        for group in re.findall(r"\(([^)]*)\)", paren_part)
    )

    brace_tuple = tuple(int(x) for x in m.group("braces").split(","))

    return bracket_tup, paren_tuples, brace_tuple

def solve_problem1(indicators: tuple[bool, ...], buttons: tuple[tuple[int, ...], ...]) -> int:
    apply_state = lambda state, button: tuple(not v if i in button else v for i, v in enumerate(state))
    n = len(indicators)
    seen_states: set[tuple[bool, ...]] = {  tuple(False for _ in range(n)) }
    states: set[tuple[bool, ...]] = { tuple(False for _ in range(n)) }
    buttons_pressed = 0

    p_state = lambda s: print("".join('#' if ind else '.' for ind in s))
    p_states = lambda sts: [ p_state(s) for s in sts ]

    while indicators not in states:
        buttons_pressed += 1
        states = {
            apply_state(state, button)
            for state in states
            for button in buttons
        }
        seen_states |= states

    return buttons_pressed


def solve1(file):
    with open(file, 'r') as f:
        sm = 0
        for line in f:
            b, pt, _ = parse_line(line.strip())
            sm += solve_problem1(b, pt)
    return sm


###########################################################################################################################################
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, value
from pulp import PULP_CBC_CMD
def solve_problem2(buttons: tuple[tuple[int, ...], ...], joltage: tuple[int, ...]) -> int:
    eqs = [
        ([ 1 if ji in b else 0 for b in buttons ], jolt)
        for ji, jolt in enumerate(joltage) ]

    n = len(buttons)
    prob = LpProblem("Minimize_Sum_of_Variables", LpMinimize)
    variables = [LpVariable(f'x{i+1}', lowBound=0, cat=LpInteger) for i in range(n)]

    prob += lpSum(variables), "Sum_of_variables"

    for coeffs, rhs in eqs:
        prob += lpSum(c*v for c, v in zip(coeffs, variables)) == rhs

    solver = PULP_CBC_CMD(msg=False)
    prob.solve(solver)
    solution = [value(v) for v in variables]
    sum_solution = sum(solution)
    return sum_solution


def solve2(file):
    with open(file, 'r') as f:
        sm = 0
        i = 0
        for line in f:
            _, pt, jolt = parse_line(line.strip())
            sm += solve_problem2(pt, jolt)
            i += 1
    return sm


print(solve1("in.small"))
print(solve1("in"))

print(solve2("in.small"))
print(solve2("in"))
