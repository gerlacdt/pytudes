# solution: https://rosettacode.org/wiki/Sum_and_Product_Puzzle#Python

from collections import Counter


PAIRS = set((x, y) for x in range(2, 100) for y in range(x + 1, 100))


def sum_pairs(n):
    '''Returns all possible pairs (a,b) which a + b == n'''
    return [(a, n-a) for a in range(2, int(n/2+1))]


def statement12(possible_pairs):
    '''
    1. Product says: i don't know the numbers.
    2. Sum says: Product does not know X and Y.
    '''
    products_counts = Counter([a * b for a, b in possible_pairs])
    uniq_products = set((a, b)
                        for a, b in possible_pairs
                        if products_counts[a * b] == 1)
    s_pairs = [(a, b) for a, b in possible_pairs
               if all((x, y) not in uniq_products
                      for (x, y) in sum_pairs(a + b))]
    return s_pairs


def statement3(possible_pairs):
    '''Product says: Now i know X and Y. Product must be unique.'''
    product_counts = Counter(a * b for a, b in possible_pairs)
    p_pairs = [(a, b) for a, b in possible_pairs if product_counts[a*b] == 1]
    return p_pairs


def statement4(possible_pairs):
    '''Sum says: Now i know X and Y, too. Sum must be unique.'''
    sum_counts = Counter(c + d for c, d in possible_pairs)
    final_pairs = [(a, b) for a, b in possible_pairs if sum_counts[a+b] == 1]
    return final_pairs


def puzzle(possible_pairs=PAIRS):
    return statement4(statement3(statement12(possible_pairs)))


if __name__ == '__main__':
    print(puzzle())
