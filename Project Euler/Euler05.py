
# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

# Personal Challenge: Smallest positive number evenly divisible 
# by all of the numbers from N1 to N2.

import timeit

start = timeit.default_timer()

smallest, n1 = 0, 0
valueFound = False

while valueFound == False:
    n1 += 2520 # We know smallest number divisible by 1-10 is 2520
    points = 0
    for i in range(2,21):
        if n1 % i != 0:
            points += 1
    if points == 0:
        smallest += n1
        valueFound = True
        
stop = timeit.default_timer()
print('Runtime: ' + str(stop - start) + 'seconds')  
print(smallest)


