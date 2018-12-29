import math
import sys
import threading

class highestPrimeFactors:




    #changes the divisor list above by populating it with the divisors of number n
    #also returns the divisor list
    #please clear the list after you use it if you only intend to use it once.
    def allFactors(self, n):

        divisor_list = []
        divisor_num = 2
        iterate_divisor = 2


        while divisor_num != 1.0:
            divisor_num = (n / iterate_divisor)


            if n % iterate_divisor == 0:
                print(str(divisor_num) + " is what we're looking at ")
                if self.isPrime(divisor_num) == True:
                    print(str(divisor_num) + " is the highest prime factor of " + str(n))
                    sys.exit()
                #print(str(iterate_divisor) + " is a factor of " + str(n))
                #stopping in the middle



                divisor_list.append(divisor_num)
            iterate_divisor += 1
            if iterate_divisor > math.ceil(n/2):
                break

        return divisor_list

    #checks to see if the divisor list is only populated by 1
    #returns True if so
    def isPrime(self, n):
        if self.allFactors(n) == [1.0]:
            #print("This number is prime")
            return True
            sys.exit()

    #initially runs all factors on number n, then iterates through said list, and in turn runs the all factors once more on iteration i, and then checks to see if iteration i is prime.
    def highestPrimeFactor_function(self,n):


        local_divisor_list = self.allFactors(n)
        for i in local_divisor_list:
            if i == 1:
                #print(n)
                print("your number is prime")
                #print("this is a prime number")
                sys.exit()
            local_divisor_list = []
            local_divisor_list = self.allFactors(i)


            if self.isPrime(i) == True:
                #print(i)
                print("This is the highest prime factor")
                sys.exit()

    def multithreadHPF(self,n):
        while True:
            self.highestPrimeFactor_function(n)


numValue = 600851475143
#numValue = 100
#object1 = highestPrimeFactors()
object2 = highestPrimeFactors()

#t1 = threading.Thread(target=object1.allFactors, args = (numValue,))

#t2 = threading.Thread(target=object2.highestPrimeFactor_function, args = (numValue,))


#t1.start()
#t2.start()



object2.highestPrimeFactor_function(numValue)
#print(object2.divisor_list)

#object1.isPrime(15)