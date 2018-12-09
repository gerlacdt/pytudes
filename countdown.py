import itertools
from collections import defaultdict, Counter
import pprint

pp = pprint.PrettyPrinter(indent=4)
operators = ('+', '-', '*', '/')

def evaluate(exp):
    "eval exp, or return None if there is an arithmetic error."
    try:
        return eval(exp)
    except ArithmeticError:
        return None

def solve_no_brackets(operators, targets):
    "All solutions to the countdown puzzle (with no brackets)"
    exps = ('10{}9{}8{}7{}6{}5{}4{}3{}2{}1'.format(*ops)
            for ops in itertools.product(operators, repeat=9))
    return {int(evaluate(exp)): exp for exp in exps if evaluate(exp) in targets}

# pp.pprint(solve_no_brackets(operators, range(1900, 2100)))

c10 = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

def splits(items):
    "Split sequence of items into two non-empty parts, in all ways."
    return [(items[:i], items[i:])
            for i in range(1, len(items))]

# pp.pprint(splits(c10))


EXPS = defaultdict(dict) # e.g., EXPS[(10, 9, 8)][27] == '((10+9)+8)'

def expressions(numbers):
    "Fill EXPS table for numbers, and all sub-sequences of numbers. Return EXPS[numbers]"
    if numbers in EXPS: # Already did the work
        pass
    elif len(numbers) == 1: # Only one way to make an expression out of a single number
        expr(numbers, numbers[0], str(numbers[0]))
    else: # Split in all ways; fill tables for left and right; combine tables in all ways
        for (Lnums, Rnums) in splits(numbers):
            for (L, R) in itertools.product(expressions(Lnums), expressions(Rnums)):
                Lexp, Rexp = '(' + EXPS[Lnums][L], EXPS[Rnums][R] + ')'
                expr(numbers, L * R, Lexp + '*' + Rexp)
                expr(numbers, L - R, Lexp + '-' + Rexp)
                expr(numbers, L + R, Lexp + '+' + Rexp)
                if R != 0:
                    expr(numbers, L / R, Lexp + '/' + Rexp)
    return EXPS[numbers]

def expr(numbers, value, exp):
    "Record exp as an expression with the given value, covering the sequence of numbers."
    EXPS[numbers][value] = exp


def countdown(n):
    return expressions(c10)[n]

if __name__ == "__main__":
    pp.pprint("2016 = {}".format(expressions(c10)[2016]))
