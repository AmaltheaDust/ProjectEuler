"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

numValue = 600851475143

import math



def isPrime(n):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    if n % 13 == 0:
        return False


    for i in reversed(range(2,int(n**0.5)+1)):
        if n%i==0:
            return False

    return True



for i in reversed(range(int(math.ceil(numValue)/2))):
    print(i)
    if i != 0 and numValue % i == 0:
        if isPrime(i) == True:
            print(i)

            break
        #else:
        #    print(i)