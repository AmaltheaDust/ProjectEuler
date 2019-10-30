# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(num):

    collatz_dict = {}

    highest_values_per_num = 0

    for i in range(num+1):
        temp_num = i
        printable_list = []

        break_value = False
        values_per_num = 0
        while break_value == False:
            printable_list.append(temp_num)
            if temp_num in collatz_dict:
                #print("i equals " + str(i))
                #print(printable_list)
                #print(str(values_per_num + collatz_dict[temp_num]) + " added value")
                if values_per_num + collatz_dict[temp_num] > highest_values_per_num:
                    highest_values_per_num = values_per_num + collatz_dict[temp_num]
                    print(i)
                    print(highest_values_per_num)
                break_value = True
            elif temp_num <= 1:
                #print("i equals " + str(i))
                #print(printable_list)
                #print(values_per_num)
                collatz_dict[i] = values_per_num
                break_value = True
            #adds a ticker so that we can "solve" our nums by using our set later on
            values_per_num += 1
            if temp_num % 2 == 0:
                temp_num = temp_num/2
            elif temp_num % 2 != 0:
                temp_num = temp_num * 3 + 1

collatz(1000000)
