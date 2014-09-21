
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is  
# 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Personal Challenge: Find largest palindrome of any two n-digit numbers.


digits = int(input('How many digits? > '))
low_end = int('1' + '0' * (digits - 1))
high_end = int('1' + '0' * digits)

pal = []
for i in range(low_end, high_end):
    for m in range(low_end, high_end):
        # print('%d * %d = %d' % (i, m, i * m))
        x = (i * m)
        if str(x) == str(x)[::-1]:
            pal.append(x)
print(max(pal))