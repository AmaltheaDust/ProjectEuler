"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""



def multiplesbelownum(numList, numBelow):

    allmultiples = []
    sumofallmultiples = 0

    for i in range(numBelow):
        for i2 in numList:
            if i % i2 == 0:
                allmultiples.append(i)
                sumofallmultiples += i
                break

    print(sumofallmultiples)
    print(allmultiples)


multiplesbelownum([3,5], 1000)