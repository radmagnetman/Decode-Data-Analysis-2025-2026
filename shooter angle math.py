import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import math

from os import listdir
from os.path import isfile, join


imgDir = r"Shooter Angle and Velocity Pictures\P 0.5" +"\\"
destDir = r"Shooter Angle and Velocity Pictures\processed\P 0.5" +"\\"

imgFiles = [f for f in listdir(imgDir) if isfile(join(imgDir, f))]

cpStore = []
#####
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[0])

# 1080x1920	
# rotation_matrix = cv2.getRotationMatrix2D([1080/2,1920/2], -10, 1)
# height, width = img.shape[:2]
# img = cv2.warpAffine(img, rotation_matrix, (width, height))


# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [784,695]
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)


plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame1')
cpStore.append(cp)

#####
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[1])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [734,645] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)


plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame2')
cpStore.append(cp)
######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[2])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [674,595] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)


plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame3')
cpStore.append(cp)

######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[3])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [614,545] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)

plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame4')
cpStore.append(cp)

######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[4])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [554,490] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)

plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame5')
cpStore.append(cp)

######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[5])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [504,440] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)

plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame6')
cpStore.append(cp)

######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[6])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)

# circle ball
cp = [444,390] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)

plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame7')
cpStore.append(cp)

######
fig, ax = plt.subplots(layout='constrained',dpi=300)
img = mpimg.imread(imgDir+imgFiles[7])

# draw reference lines
cv2.line(img,[1057,954], [48,1006], (0,255,0), thickness = 3)
cv2.line(img,[1057,954], [1004,73], (0,255,0), thickness = 3)

# draw 1 inch square
ul = [210,941]
lr = [267,995]
ur = [210,995]
ll = [267,941]
cv2.line(img,ul, ur, (0,255,0), thickness = 3)
cv2.line(img,ur, lr, (0,255,0), thickness = 3)
cv2.line(img,lr, ll, (0,255,0), thickness = 3)
cv2.line(img,ll, ul, (0,255,0), thickness = 3)


# circle ball
cp = [444-50,390-50] # delta -50,-50
cv2.circle(img, cp, 250,  (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0]-50,cp[1]],[cp[0]+50,cp[1]], (255, 0, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,[cp[0],cp[1]-50],[cp[0],cp[1]+50], (255, 0, 0), thickness=5, lineType=8, shift=0)

for i in range(len(cpStore)-1):
    cv2.line(img,cpStore[i],cpStore[i+1], (255, 255, 0), thickness=5, lineType=8, shift=0)
    print("%d %d" % (cpStore[i][0],cpStore[i][1]))
    cv2.circle(img, cpStore[i], 10,  (255, 255, 0), thickness=5, lineType=8, shift=0)
cv2.circle(img, cpStore[-1], 10,  (255, 255, 0), thickness=5, lineType=8, shift=0)
cv2.line(img,cpStore[-1],cp, (255, 255, 0), thickness=5, lineType=8, shift=0)

plt.imshow(img)
# plt.show()
fig.savefig(destDir+'frame8')
cpStore.append(cp)

frameRate = 240 # FPS
dt = 1/frameRate

dx = cpStore[-1][0] - cpStore[0][0]
dy = cpStore[-1][1] - cpStore[0][1]
dy1in = (995-941)*4
dx1in = (267-210)*4

dx_in = dx/dx1in
dy_in = dy/dy1in
d = (dx_in**2+dy_in**2)**0.5
print('dx: %0.1f\ndy: %0.1f\n d: %0.1f' % (dx_in,dy_in,d))
print('dt: %0.1f ms' % (dt*1000))
print('v: %0.1f m/s' % (d/dt/39.3701))

V = 1000 # ticks/sec
diam = 96/1000 # m
circ = 3.1415*diam # m
ticksPerRev = 28
vel = V/ticksPerRev*circ
print('Angular v: %0.1f' % (vel/2))

# P12 = sqrt((P1x - P2x)2 + (P1y - P2y)2)
# arccos((P12^2 + P13^2 - P23^2) / (2 * P12 * P13))

# p1 = [1057,954]
# p2 = [48,1006]
# p3 = [1004,73]

# P12 = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
# P13 = ((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)**0.5
# P23 = ((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)**0.5
# angle_rad = math.acos((P12**2 + P13**2 + P23**2) / (2*P12*P13))
# angle_deg = angle_rad*57.296
# print(angle_deg)

front = [[631,1319],[990,1225]]
back = [[655,1215],[911,1141]]

dFront = ((990-631)**2+(1225-1319)**2)**0.5
dBack = ((911-655)**2+(1141-1215)**2)**0.5
dAvg = (dFront+dBack)/2 # pixels
dAvg = dAvg/82.425 # px/mm

dx = cpStore[-1][0] - cpStore[0][0]
dy = cpStore[-1][1] - cpStore[0][1]
dpx = (dx**2+dy**2)**0.5

d = dpx/dAvg/1000 # m
t = 8/240

print('%0.1f' % (d/t))