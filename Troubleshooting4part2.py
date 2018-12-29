"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from functools import reduce


#determines if palindrome

def palindromeChecker(value):

    if list(str(value)) == list(reversed(str(value))):
        print(value)
        print("this is a palindrome")

#function that multiplies all arguments inside the list argument, also might just be provided as a one liner later
def multiplyAllItemsInList(listvalue):
    testvar = reduce(lambda x, y: x * y, listvalue)
    return testvar


def productPossibilities(numberofdigits, maxiteratorvalue):

    #preps our list of values
    LOD = []
    LOT = []

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

            #TODO unsure why LOD is not behaving like a value here.
            LOT = list(LOD)

            #LOD[listsize] -= 1

            print("number value iteration number: " + str(i))
            print("")

            for i2 in reversed(range(maxiteratorvalue+1)):




                if i2 == 0:

                    break

                #TODO also unsure why printing LOT or LOD appears the same whether I put LOT = LOD or LOD = LOT above
                print(LOT)

                #currently working on this section to "countdown"
                LOT[listsize] -= 1

                if LOT[listsize] == 0:
                    LOD[listsize - 1] -= 1


                print("    max value iteration number: " + str(i2))
            print()


productPossibilities(2,5)