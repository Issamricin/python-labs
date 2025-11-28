"""Calculates sums of arithmetic and geometric sequences"""

from typing import Union

Number = Union[int, float] # define a type


def arithmetic_sum(a1: Number, d: Number, n: int) -> float:
    """Returns the sum of the first n terms of an arithmetic sequence.
    Formula: a_n = a1 + d * (n-1); S= n * (a1 + an) / 2"""
    pass


def geometric_sum(g1: Number, q: Number, n: int) -> float:
    """Returns the sum of the first n terms of a geometric sequence.
    Om q != 1: S = g1 * (q**n - 1) / (q - 1)
    om q == 1: S = n * g1"""
    pass


def main() -> None:
    """Inserts values into the sequences"""

    # Arithmetic: a1=1, d=1, n=4 => 1 + 2 + 3 + 4 = 10
    a_sum = arithmetic_sum(a1=1, d=1, n=4)

    # Geometric: g1=1, q=2, n=5 => 1 + 2 + 4 + 8 + 16 = 31
    g_sum = geometric_sum(g1=1, q=2, n=5)

    print(f"the arithmetic sum is: {a_sum:.0f}")
    print(f"the geometric sum is: {g_sum:.0f}")


if __name__ == "__main__":
    main()
    exit(0)