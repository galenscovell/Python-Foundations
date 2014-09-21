
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.

# Personal Challenge: Find the sum of all multiples of 3 or 5 below input value.

sumList = []
limit = int(input('Find the sum of all multiples of 3 or 5 below which number? > '))

for i in range(1, limit):
    if i % 3 == 0 or i % 5 == 0:
        sumList.append(i)
print(sum(sumList))

