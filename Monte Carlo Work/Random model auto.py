# Random auto model
import random
import sys
import statistics

class classifier:
    def __init__(self,inputPattern):
        #self.currentScore = 0
        self.classifier = ['e','e','e','e','e','e','e','e','e']
        self.pattern = inputPattern
        self.firstEmpty = 0
        
    def classifyBonus(self):
        bonus = 0
        for i in range(len(self.pattern)):
            if self.pattern[i] == self.classifier[i]:
                bonus += 2
        return bonus
    
    def returnNumMatches(self):
        numMatches = 0
        for i in range(len(self.pattern)):
            if self.pattern[i] == self.classifier[i]:
                numMatches += 1
        return numMatches

    def addShot(self,shot):
        shotScore = 0
        for i in range(len(shot)):
            if shot[i] != 'e':
                if self.firstEmpty < 9:
                    shotScore += 3
                    self.classifier[self.firstEmpty] = shot[i]
                    self.firstEmpty += 1
                    if self.firstEmpty == 9:
                        self.firstEmpty = 9
                else:
                    shotScore += 1
        return shotScore
        
    def openGate(self):
        self.classifier = ['e','e','e','e','e','e','e','e','e']
        self.firstEmpty = 0

    def printClassifier(self):
        outStr = ''
        spaceCount = 0
        for i in range(len(self.classifier)):
            if self.classifier[i] != 'e':
                outStr += self.classifier[i]
            if spaceCount == 2:
                outStr += ' '
                spaceCount = 0
            else:
                spaceCount += 1
        
        if outStr[-1] == ' ':
            outStr = outStr[:-1]
        
        while len(outStr) < 11:
            outStr += ' '
        
        p1 = self.pattern[0] + self.pattern[1] + self.pattern[2]
        p2 = self.pattern[3] + self.pattern[4] + self.pattern[5]
        p3 = self.pattern[6] + self.pattern[7] + self.pattern[8]
        print('   Pattern [ ' + p1 + ' ' + p2 + ' ' + p3 + ' ]')
        print('Classifier [ ' + outStr + ' ]')
            

def randomPattern():
    pattern1 = ['p','p','g','p','p','g','p','p','g']
    pattern2 = ['p','g','p','p','g','p','p','g','p']
    pattern3 = ['g','p','p','g','p','p','g','p','p']
    num = random.random()
    if num <= (1/3):
        pattern = pattern1
    elif num <= (2/3) and num > (1/3):
        pattern = pattern2
    else:
        pattern = pattern3
    
    return pattern

def createShot(thisShot, **kwargs):
    # print('func: ' + thisShot[0]+thisShot[1]+thisShot[2])
    probHit = [1,1,1]
    probFlip = 0
    for key, value in kwargs.items():
        if key == 'probHit':
            probHit = value
        elif key == 'probFlip':
            probFlip = value
        else:
            print("Invalid argument: %s" % (key))
            sys.exit(1)
    
    if len(thisShot) != 3:
        print('Shots consist of 3 values: %d were given' % (len(thisShot)))
        sys.exit(1)
    
    if thisShot.count('e') > 0:
        print('Empty ball in shot')
        sys.exit(1)
    
    for i in range(len(thisShot)):
        num = random.random()
        if num > probHit[i]:
            thisShot[i] = 'e'
    
    if thisShot[0] == 'e':
        thisShot[0] = thisShot[1]
        thisShot[1] = thisShot[2]
        thisShot[2] = 'e'
    
    if thisShot[1] == 'e':
        thisShot[1] = thisShot[2]
        thisShot[2] = 'e'
        
    if random.random() < probFlip:
        temp = thisShot[0]
        thisShot[0] = thisShot[1]
        thisShot[1] = temp

    if random.random() < probFlip:
        temp = thisShot[1]
        thisShot[1] = thisShot[2]
        thisShot[2] = temp

    if thisShot[0] == 'e':
        thisShot[0] = thisShot[1]
        thisShot[1] = thisShot[2]
        thisShot[2] = 'e'
    
    if thisShot[1] == 'e':
        thisShot[1] = thisShot[2]
        thisShot[2] = 'e'
    
    return thisShot
    

# grab ball's pos 0 -> 2
preload = ['g','p','p']
fieldLoc1 = ['g','p','p']
fieldLoc2 = ['p','g','p']
fieldLoc3 = ['p','p','g']
corner = ['p','g','p']

#---- Full match
probToFlip = 0
probToHit = [1,1,1]

runningAutoScore = []
runningAutoMatches = []

runningTeleopScore = []
runningTeleopMatches = []

runningTotalScore = []
runningTotalMatches = []

for i in range(10000):
    score = 0
    p = randomPattern()
    c = classifier(p)

    currentLoad = ['g','p','p']
    shot1 = createShot(currentLoad,probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot1)

    c.openGate()

    currentLoad = ['g','p','p']
    shot2 = createShot(currentLoad,probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot2)

    currentLoad = ['p','g','p']
    shot3 = createShot(currentLoad,probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot2)

    currentLoad = ['p','p','g']
    shot4 = createShot(currentLoad,probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot2)

    score += c.classifyBonus()
    runningAutoScore.append(score)
    runningAutoMatches.append(c.returnNumMatches())

    score = 0
    
    c.openGate()

    for j in range(9):
        shot = createShot(['p','p','g'],probFlip = probToFlip,probHit = probToHit)
        score += c.addShot(shot)
        if (j+1) % 3 == 0:
            c.openGate()
    

    shot = createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot)
    
    shot = createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot)
    
    shot = createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit)
    score += c.addShot(shot)
    
    score += c.classifyBonus()
    runningTeleopScore.append(score)
    runningTeleopMatches.append(c.returnNumMatches())

    runningTotalScore.append(runningAutoScore[-1] + runningTeleopScore[-1])
    runningTotalMatches.append(runningAutoMatches[-1] + runningTeleopMatches[-1])
        

    


print('-----')
print('   Avg auto score: %0.1f +/- %0.1f' % (statistics.mean(runningAutoScore),statistics.stdev(runningAutoScore)))
print(' Num auto matches: %0.1f +/- %0.1f' % (statistics.mean(runningAutoMatches),statistics.stdev(runningAutoMatches)))
print('   Avg tele score: %0.1f +/- %0.1f' % (statistics.mean(runningTeleopScore),statistics.stdev(runningTeleopScore)))
print(' Num tele matches: %0.1f +/- %0.1f' % (statistics.mean(runningTeleopMatches),statistics.stdev(runningTeleopMatches)))
print('  Avg total score: %0.1f +/- %0.1f' % (statistics.mean(runningTotalScore),statistics.stdev(runningTotalScore)))
print('Num total matches: %0.1f +/- %0.1f' % (statistics.mean(runningTotalMatches),statistics.stdev(runningTotalMatches)))


#---- Sorting Auto
# probToFlip = 0
# probToHit = [1,1,1]
# runningScore = []
# runningMatches = []
# for i in range(10000):
#     score = 0
#     p = randomPattern()
#     c = classifier(p)
    
#     sortedShot = p[0:3]
#     shot1 = createShot(sortedShot,probFlip = probToFlip,probHit = probToHit)

#     sortedShot = p[0:3]
#     shot2 = createShot(sortedShot,probFlip = probToFlip,probHit = probToHit)
    
#     sortedShot = p[0:3]
#     shot3 = createShot(sortedShot,probFlip = probToFlip,probHit = probToHit)

#     score += c.addShot(shot1)
#     score += c.addShot(shot2)
#     score += c.addShot(shot3)
#     # score += c.addShot(createShot(sortedShot,probFlip = probToFlip,probHit = probToHit))

#     score += c.classifyBonus()
#     runningScore.append(score)
#     runningMatches.append(c.returnNumMatches())

# print('-----')
# print('  Avg score: %0.1f +/- %0.1f' % (statistics.mean(runningScore),statistics.stdev(runningScore)))
# print('Num matches: %0.1f +/- %0.1f' % (statistics.mean(runningMatches),statistics.stdev(runningMatches)))



