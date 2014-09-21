
# Take any natural number n. If n is even, divide it by 2. If n is 
# odd, multiply it by 3 and add 1. Repeat the process. The conjecture  
# is that no matter what number you start with, you will always  
# eventually reach 1 (oneness).

def collatz(n, r):
    while n != 1:
        if (n % 2) == 0:
            r += 1
            n /= 2
        elif (n % 2) != 0:
            r += 1
            n = (n * 3) + 1
    else:
        print('Reached %d in %d steps.' % (n, r))
        quit()

n = 0
r = 0
while n <= 1:
    n = int(input('Natural number n (> 1): '))
collatz(n, r)
