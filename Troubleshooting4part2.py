"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from functools import reduce


#determines if palindrome

def palindromeChecker(value):

    if list(str(value)) == list(reversed(str(value))):
        return True

#function that multiplies all arguments inside the list argument, also might just be provided as a one liner later
def multiplyAllItemsInList(listvalue):
    testvar = reduce(lambda x, y: x * y, listvalue)
    return testvar


def productPossibilities(numberofdigits, maxiteratorvalue):

    #preps our list of values
    LOD = []
    LOT = []
    finalvalue = 0

    #creates list of values, at the specified maxiteration
    for i in range(numberofdigits):
        LOD.append(maxiteratorvalue)
        LOT.append(maxiteratorvalue)




    listsize_external = 1

    #iterate as many times as the maxiteratorvalue, in this instance, 5 times.

    for listsize in reversed(range(numberofdigits)):
        if listsize == 0:
            break

        print("listsize iteration number: " + str(listsize))

        for i in reversed(range(maxiteratorvalue+1)):





            LOT = list(LOD)

            if i == 0:
                break

            print("number value iteration number: " + str(i))
            print("")

            for i2 in reversed(range(maxiteratorvalue+1)):

                if i2 == 0:

                    break

                print(LOT)
                if palindromeChecker(multiplyAllItemsInList(LOT)) == True:
                    if multiplyAllItemsInList(LOT) > finalvalue:
                        finalvalue = multiplyAllItemsInList(LOT)
                        finallist = list(LOT)

                #currently working on this section to "countdown"
                LOT[listsize] -= 1

                if LOT[listsize] == 0:
                    LOD[listsize - 1] -= 1




                print("    value of i2 within maxiteratorvalue: " + str(i2))
            print()

    print(finalvalue)
    print(finallist)

productPossibilities(2,999)