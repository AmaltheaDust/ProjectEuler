import math
import sys
import threading

class highestPrimeFactors:

    divisor_list = []


    #changes the divisor list above by populating it with the divisors of number n
    #also returns the divisor list
    #please clear the list after you use it if you only intend to use it once.
    def allFactors(n):

        divisor_list = []
        divisor_num = 2
        iterate_divisor = 2
        test_divisor_num = 0

        while divisor_num > 1:

            if n % iterate_divisor == 0:
                divisor_num = (n / iterate_divisor)
                print(divisor_num)

                if n % divisor_num == 0:
                    if test_divisor_num != divisor_num:
                        # print(divisor_num)

                        self.divisor_list.append(divisor_num)

                    test_divisor_num = divisor_num

                iterate_divisor += 1

            else:
                iterate_divisor += 1
                continue

        return self.divisor_list

    #checks to see if the divisor list is only populated by 1
    #returns True if so
    def isPrime(self, n):
        if self.divisor_list == [1]:
            #print("This number is prime")
            return True

    #initially runs all factors on number n, then iterates through said list, and in turn runs the all factors once more on iteration i, and then checks to see if iteration i is prime.
    def highestPrimeFactor_function(self,n):

        self.divisor_list = []
        self.allFactors(n)
        for i in self.divisor_list:
            if i == 1:
                print(n)
                print("your number is prime")
                #print("this is a prime number")
                sys.exit()
            self.divisor_list = []
            self.allFactors(i)

            if self.isPrime(i) == True:
                print(i)
                print("This is the highest prime factor")
                sys.exit()

    def multithreadHPF(self,n):
        while True:
            self.highestPrimeFactor_function(n)


numValue = 600851475143

object1 = highestPrimeFactors()

t1 = threading.Thread(target=object1.allFactors, args = (numValue,))
t2 = threading.Thread(target=object1.multithreadHPF, args = (numValue,))


t1.start()
t2.start()
print(object1.divisor_list)


#object2.highestPrimeFactor_function(600851475143)
#print(object2.divisor_list)

#object1.isPrime(15)

"""

def allFactors(n):


    divisor_list = []
    divisor_num = 2
    iterate_divisor = 2
    test_divisor_num = 0

    while divisor_num > 1:

        if n % iterate_divisor == 0:
            divisor_num = (n / iterate_divisor)
            print(divisor_num)

            if n % divisor_num == 0:
                if test_divisor_num != divisor_num:

                    #print(divisor_num)

                    divisor_list.append(divisor_num)

                test_divisor_num = divisor_num

            iterate_divisor += 1

        else:
            iterate_divisor += 1
            continue

    return divisor_list

allFactors(10)

"""