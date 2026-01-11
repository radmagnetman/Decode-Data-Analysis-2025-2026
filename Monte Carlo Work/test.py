# Random auto model
import random
import sys
import statistics as st
import math

from numpy import roll


# Roll D6, if >= 3 roll D20, if 1-2 roll D10
# What is probability that you get above an 8

def rolldice(numSides):
    return math.ceil(random.random()*numSides)


didMakeIt = []

for i in range(100000):
    if rolldice(6) >= 3:
        if rolldice(20) > 8:
            didMakeIt.append(1)
        else:
            didMakeIt.append(0)
    else:
        if rolldice(10) > 8:
            didMakeIt.append(1)
        else:
            didMakeIt.append(0)


print('avg event: %0.1f%% +/- %0.1f%%' % (st.mean(didMakeIt)*100,st.stdev(didMakeIt)*100))










































# storeArray = []

# for i in range(10000):
#     storeArray.append(rolldice(6)+rolldice(6))

# print('%0.1f +/- %0.1f' %(st.mean(storeArray),st.stdev(storeArray)))
