"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sumofsquares(num):
    squarenum = 0
    for i in range(num+1):
        squarenum += i**2
    return squarenum

def squareofsum(num):
    sumnum = 0
    for i in range(num+1):
        sumnum += i
    return sumnum ** 2

numnum = 100
print(squareofsum(numnum) - sumofsquares(numnum))

