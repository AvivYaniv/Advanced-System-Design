import math
from functools import reduce

"""
    Reducing each time the multiplies of the current number from the initial list, which contains all numbers from 2 to n
"""
def sieve_of_eratosthenes(n):
    return reduce(lambda s, x: s - set(range(x*x, n, x)) if x in s else s, range(2, int(math.sqrt(n)) + 1), set(range(2,n)))

if __name__ == '__main__':
    import sys
    print(sieve_of_eratosthenes(int(sys.argv[1])))
    sys.exit()
