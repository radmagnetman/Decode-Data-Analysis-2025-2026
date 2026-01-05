# Random model
import random
import statistics

pattern1 = ['p','p','g','p','p','g','p','p','g']
pattern2 = ['p','g','p','p','g','p','p','g','p']
pattern3 = ['g','p','p','g','p','p','g','p','p']

pattern = pattern1

matchTotal = []
for j in range(100000):
    matchTally = 0
    totalG = 12
    totalP = 24
    for i in range(len(pattern)):
        num = random.random()
        fG = totalG/(totalG+totalP)
        fP = totalP/(totalG+totalP)
        if num < fG:
            picked = 'g'
            totalG = totalG-1
        else:
            picked = 'p'
            totalP = totalP-1
        
        if(pattern[i] == picked):
            matchTally += 1
    matchTotal.append(matchTally)

print('%0.1f +/- %0.1f' % (statistics.mean(matchTotal),statistics.stdev(matchTotal)))
