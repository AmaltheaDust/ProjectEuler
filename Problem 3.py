import math
import sys


class highestPrimeFactors:

    # changes the divisor list above by populating it with the divisors of number n
    # also returns the divisor list
    # please clear the list after you use it if you only intend to use it once.
    def allFactors(self, n):

        divisor_list = []

        divisor_num = 2
        iterate_divisor = 2
        test_divisor_num = 0

        while divisor_num > 1:

            if n % iterate_divisor == 0:
                divisor_num = (n / iterate_divisor)
                if divisor_num == 1:
                    sys.exit()
                print(divisor_num)

                if self.isPrime(divisor_num) == True:
                    print(str(divisor_num) + " is the highest prime factor of " + str(n))
                    sys.exit()

                if n % divisor_num == 0:
                    if test_divisor_num != divisor_num:
                        # print(divisor_num)

                        divisor_list.append(divisor_num)

                    test_divisor_num = divisor_num

                iterate_divisor += 1

            else:
                iterate_divisor += 1
                continue

        return divisor_list

    # checks to see if the divisor list is only populated by 1
    # returns True if so
    def isPrime(self, n):
        if self.allFactors(n) == [1.0]:
            print("This number is prime")
            return True

    # initially runs all factors on number n, then iterates through said list, and in turn runs the all factors once more on iteration i, and then checks to see if iteration i is prime.
    def highestPrimeFactor(self, n):
        local_divisor_list = []
        local_divisor_list = self.allFactors(n)
        for i in self.divisor_list:
            if i == 1:
                print(n)
                print("your number is prime")
                # print("this is a prime number")
                # sys.exit()
            local_divisor_list = []
            local_divisor_list = self.allFactors(i)

            if self.isPrime(i) == True:
                print(i)
                print("This is the highest prime factor")
                sys.exit()


object1 = highestPrimeFactors()
object2 = highestPrimeFactors()

numValue = 13195
# numValue = 600851475143

object2.highestPrimeFactor(numValue)
# print(object2.divisor_list)

# object1.isPrime(15)