"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

numValue = 13195

import math

for i in reversed(range(math.ceil(numValue)/2)):
    if numValue % i == 0:
        if isprime(i) == True:
            print("The largest prime factor of " + str(numValue) + " is " str(i))

            break
        else:
            continue

def isprime(aNumber):
    if aNumber % 2 == 0:
        return False
    if aNumber % 3 == 0:
        return False
    if aNumber % 5 == 0:
        return False
    if aNumber % 7 == 0:
        return False
    if aNumber % 11 == 0:
        return False

    else:
        for i in math.ceil(aNumber/2):
            if (aNumber/2) % i == 0 and i != 1:
                return True
            else:
                return True
