# Random model
import random
import statistics

pattern = ['p','p','g','p','p','g','p','p','g']

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

print(statistics.mean(matchTotal))
print(statistics.stdev(matchTotal))