# The sum of the squares of the first ten natural numbers is, 
#       1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

# Personal Challenge: User defined limit.

import timeit

limit1 = int(input('Beginning value? > '))
limit2 = int(input('End value? > ')) + 1
sumS, sqrS = 0, 0
start = timeit.default_timer()

for i in range(limit1, limit2):
    iSqr = i ** 2
    sumS += iSqr

sqrS = sum(range(limit1, limit2)) ** 2

print('\nDifference between sum of the squares and square of the sum is ' + str(sqrS - sumS) + '.\n')
stop = timeit.default_timer()
print('Runtime: ' + str(stop - start) + 'seconds\n')