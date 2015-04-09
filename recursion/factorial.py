import numpy as np


class Factorial():
    def recursive_factorial(self, n):
        n = np.uint64(n)

        if n == 0 or n == 1:
            return 1
        else:
            return n * self.recursive_factorial(n-1)

    def tail_recursive_factorial(self, n, r=1):
        n = np.uint16(n)
        r = np.uint64(r)

        if n == 0:
            return 1
        if n == 1:
            return r
        else:
            return self.tail_recursive_factorial(n - 1, n * r)

    def iterative_factorial(self, n):
        n = np.uint16(n)
        r = np.uint64(1)

        for i in np.arange(n, 1, -1):
            r *= i

        return r
