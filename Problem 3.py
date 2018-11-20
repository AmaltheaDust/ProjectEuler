"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

numValue = 600851475143

import math
import threading
import sys
"""
def isPrimeFactor(n):
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

"""



divisor_list = []

class highestPrimeFactors:



    def allFactors(self, n):

        global divisor_list

        divisor_num = 2

        iterate_divisor = 2

        test_divisor_num = 0



        while divisor_num > 1:

            divisor_num = int(math.floor(n / iterate_divisor))
            #print(divisor_num)
            if n % divisor_num == 0:



                if test_divisor_num != divisor_num:

                    print(divisor_num)

                    divisor_list.append(divisor_num)

                test_divisor_num = divisor_num

                #return True

            iterate_divisor += 1

        return divisor_list

    def isPrime(self, n):
        if self.allFactors(n) == [1]:
            print("This number is prime")
            return True

    def highestPrimeFactor(self):

        global divisor_list

        while True:
            for i in divisor_list:
                if self.isPrime(i) == True:
                    print("This is the highest prime factor")
                    sys.exit()




object1 = highestPrimeFactors()
object2 = highestPrimeFactors()


t1 = threading.Thread(target=object1.isPrime, args = (13,))
t2 = threading.Thread(target=object2.highestPrimeFactor)

t1.start()
t2.start()

#object1.isPrime(13)

