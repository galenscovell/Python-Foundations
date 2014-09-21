
# This is a game of Craps. It uses two dice and follows a simple system.
# On the first roll 2, 3, or 12 = loss while 7 or 11 = win. Anything else = point.
# In the next rolls the goal is to roll the point. If you roll a 7, you lose.

import random

def main(counts):
    while counts[2] != counts[3]:
        total_1 = random.randint(1, 6) + random.randint(1, 6)
        if total_1 in (2, 3, 12):
            counts[2] += 1
            counts[1] += 1
            main(counts)
        elif total_1 in (7, 11):
            counts[2] += 1
            counts[0] += 1
            main(counts)
        else:
            total_2 = 0
            while total_2 not in (total_1, 7):
                total_2 = random.randint(1, 6) + random.randint(1, 6)
            if total_2 == total_1:
                counts[2] += 1
                counts[1] += 1
                main(counts)
            elif total_2 == 7:
                counts[2] += 1
                counts[0] += 1
                main(counts)        
    print('Win/loss ratio: %d/%d\nPlays: %d\n' % (counts[0], counts[1], counts[2]))
    quit()

counts = [0, 0, 0]
counts.append( int(input('Number of automated runs: ')) )
main(counts)