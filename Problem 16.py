"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

mynum = 2**1000
#print(mynum)
digitsum = 0
for i in str(mynum):
    #print(i)
    digitsum += int(i)

print(digitsum)
