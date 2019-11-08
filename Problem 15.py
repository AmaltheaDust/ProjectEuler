"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

end value -
n+1 x 2

6**2 - 2**3

6 paths through 2x2

20 paths through 3x3

70 paths through 4x4

2by2 offers 1 center,


"""

from math import factorial
fa = factorial
n=20

print(fa(2*n) /
     (fa(n)**2))
