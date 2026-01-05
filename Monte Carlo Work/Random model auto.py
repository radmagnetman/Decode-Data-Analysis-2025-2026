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

def createShot(shot, **kwargs):
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
    
    if len(shot) != 3:
        print('Shots consist of 3 values: %d were given' % (len(shot)))
        sys.exit(1)
    
    if shot.count('e') > 0:
        print('Empty ball in shot')
        sys.exit(1)
    
    for i in range(len(shot)):
        num = random.random()
        if num > probHit[i]:
            shot[i] = 'e'
    
    if shot[0] == 'e':
        shot[0] = shot[1]
        shot[1] = shot[2]
        shot[2] = 'e'
    
    if shot[1] == 'e':
        shot[1] = shot[2]
        shot[2] = 'e'
        
    if random.random() < probFlip:
        temp = shot[0]
        shot[0] = shot[1]
        shot[1] = temp

    if random.random() < probFlip:
        temp = shot[1]
        shot[1] = shot[2]
        shot[2] = temp

    if shot[0] == 'e':
        shot[0] = shot[1]
        shot[1] = shot[2]
        shot[2] = 'e'
    
    if shot[1] == 'e':
        shot[1] = shot[2]
        shot[2] = 'e'
    
    return shot
    

# grab ball's pos 0 -> 2
preload = ['g','p','p']
fieldLoc1 = ['g','p','p']
fieldLoc2 = ['p','g','p']
fieldLoc3 = ['p','p','g']
corner = ['p','g','p']

probToFlip = .1
probToHit = [.9,.9,.9]
runningScore = []
runningMatches = []
for i in range(5):
    score = 0
    p = randomPattern()
    c = classifier(p)
    sortedShot = p[0:3]
    score += c.addShot(createShot(sortedShot,probFlip = probToFlip,probHit = probToHit))
    score += c.addShot(createShot(sortedShot,probFlip = probToFlip,probHit = probToHit))
    score += c.addShot(createShot(sortedShot,probFlip = probToFlip,probHit = probToHit))
    score += c.classifyBonus()
    runningScore.append(score)
    runningMatches.append(c.returnNumMatches())

c.printClassifier()
print('  Avg score: %0.1f +/- %0.1f' % (statistics.mean(runningScore),statistics.stdev(runningScore)))
print('Num matches: %0.1f +/- %0.1f' % (statistics.mean(runningMatches),statistics.stdev(runningMatches)))

# numLoops = 10000
# scoreTotal = []
# matchTotal = []

# probToHit = [.7,.9,.8]
# probToFlip = 0

# for i in range(numLoops):
#     currentScore = score(randomPattern())
#     currentScore.addShot(['g','p','p'])
#     currentScore.openGate()
#     currentScore.addShot(createShot(['g','p','p'],probFlip = probToFlip,probHit = probToHit))
#     currentScore.addShot(createShot(['p','g','p'],probFlip = probToFlip,probHit = probToHit))
#     currentScore.addShot(createShot(['p','p','g'],probFlip = probToFlip,probHit = probToHit))
#     numMatchesInAuto = currentScore.returnNumMatches()
#     currentScore.addClassifiyBonus()
#     currentScore.openGate()
    
#     for j in range(5):
#         currentScore.addShot(createShot(['p','g','p'],probFlip = probToFlip,probHit = probToHit))
#         currentScore.addShot(createShot(['p','g','p'],probFlip = probToFlip,probHit = probToHit))
#         currentScore.addShot(createShot(['p','g','p'],probFlip = probToFlip,probHit = probToHit))
#         currentScore.openGate()
    
#     currentScore.addShot(createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit))
#     currentScore.addShot(createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit))
#     currentScore.addShot(createShot(['p','p','p'],probFlip = probToFlip,probHit = probToHit))
#     currentScore.addClassifiyBonus()


#     scoreTotal.append(currentScore.returnScore(True))
#     matchTotal.append(currentScore.returnNumMatches()+numMatchesInAuto)


# print('  Avg score: %0.1f +/- %0.1f' % (statistics.mean(scoreTotal),statistics.stdev(scoreTotal)))
# print('Num matches: %0.1f +/- %0.1f' % (statistics.mean(matchTotal),statistics.stdev(matchTotal)))

# #currentScore.printClassifier()
# #print('  Score: %d' % (currentScore.returnScore(True)))
# #print('Matches: %d' % (currentScore.returnNumMatches()))


# # Situation 1, grab field loc 1, 2, 3, empty, grab corner

# # for i in range(10000):
# #     score = 0
# #     thisPattern = randomPattern()


