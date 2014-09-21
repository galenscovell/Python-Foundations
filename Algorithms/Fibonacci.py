
# Fibonacci sequence from 1 to given limit.

limit = int(input('Fibonacci series to what upper limit? '))
a, b = 0, 1

while b < limit:
    print(b)
    a, b = b, a + b

