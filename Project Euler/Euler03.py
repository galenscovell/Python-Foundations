
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Personal challenge: Find all prime factors of an input value.

value = int(input('\nNumber of interest: '))

factors = [] 
j = 2
while value > 1:
    while (value % j) == 0:
        factors.append(j)
        value /= j
    j += 1
print('\nPrime factors are: %s \nLargest Prime Factor is: %s\n' % (factors, max(factors)))



