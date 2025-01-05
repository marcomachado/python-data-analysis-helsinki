#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    return (x1,x2)


def main():
    print(solve_quadratic(1.115385,9.419240,7.415749))
    """
    np.float64(-1.548535003254413) != 0 within 4 places 
    (np.float64(1.548535003254413) difference) : -1.093222 
    is not a solution for equation 1.115385*x**2 + 9.419240*x + 7.415749 == 0!
    """

if __name__ == "__main__":
    main()
