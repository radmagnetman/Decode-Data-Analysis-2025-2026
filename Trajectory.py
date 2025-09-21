import numpy as np
import matplotlib.pyplot as plt

g = 9.84 # m/s2
# alphaRange = [15,30,45,60,75]
# #alpha = np.deg2rad(45)
# h = 16 # in
# h = h*2.54/100 # m

# wheelDiameter = 96 / 1000       # m
# circum = 3.1415*wheelDiameter   # m
# rpm = 1150
# V0 = rpm/60*circum              # m/s

# print("V0: %0.1f m/s" % V0)

# xft = np.linspace(0,140,1000)
# xm = [float(x*0.3048) for x in xft]

# fig, ax1 = plt.subplots(layout='constrained',dpi=300)
# for alpha in alphaRange:
#     ym = [float( h + x*np.tan(alpha)-g*(x**2)/(2*V0**2*(np.cos(alpha)**2)) ) for x in xm]
#     yft = [float(y/0.3048) for y in ym]
#     ax1.plot(xft, yft,label = alpha)

# ax1.set_xlim(0,20)
# ax1.set_ylim(0,5)
# ax1.set_xlabel('Horizontal distance (ft)')
# ax1.set_ylabel('Vertical distance (ft)')
# ax1.legend()
# fig.savefig('by angle')

#######
# alpha = np.deg2rad(35) # angle from horz
# h = 16 # in
# h = h*2.54/100 # m

# wheelDiameter = 96 / 1000       # m
# circum = 3.1415*wheelDiameter   # m
# rpm = 6000/2
# pfRange = [.2,.4,.45,.5,.55,.6]


# print("V0: %0.1f m/s" % V0)

# xft = np.linspace(0,140,1000)
# xm = [float(x*0.3048) for x in xft]

# fig, ax1 = plt.subplots(layout='constrained',dpi=300)
# for p in pfRange:
#     V0 = p*rpm/60*circum              # m/s
#     ym = [float( h + x*np.tan(alpha)-g*(x**2)/(2*V0**2*(np.cos(alpha)**2)) ) for x in xm]
#     yft = [float(y/0.3048) for y in ym]
#     ax1.plot(xft, yft,label = p)

# goalHeight1 = 38.75/12
# goalHeight2 = (38.75+15)/12
# goalDist1 = ((2.5*2)**2 + (4.5*2)**2)**0.5-2
# goalDist2 = ((3*2)**2 + (5*2)**2)**0.5-2
# ax1.plot([goalDist1,goalDist1],[0,goalHeight1],'k',linewidth = 3)
# ax1.plot([goalDist2,goalDist2],[0,goalHeight2],'k',linewidth = 3)


# ax1.set_xlim(0,20)
# ax1.set_ylim(0,5)
# ax1.set_xlabel('Horizontal distance (ft)')
# ax1.set_ylabel('Vertical distance (ft)')
# ax1.legend()
# fig.savefig('by power')

# # plt.show()

##################
alpha = 45
alpha = np.deg2rad(45)
h = 15 # in
h = h*2.54/100 # m

wheelDiameter = 96 / 1000       # m
circum = 3.1415*wheelDiameter   # m
rpm = 1150
V0 = rpm/60*circum              # m/s

print("V0: %0.1f m/s" % V0)

xft = np.linspace(0,140,1000)
xm = [float(x*0.3048) for x in xft]

fig, ax1 = plt.subplots(layout='constrained',dpi=300)
ym = [float( h + x*np.tan(alpha)-g*(x**2)/(2*V0**2*(np.cos(alpha))**2) ) for x in xm]
yft = [float(y/0.3048) for y in ym]
ax1.plot(xft, yft,label = alpha)



ax1.set_xlim(0,20)
ax1.set_ylim(0,6)
ax1.set_xlabel('Horizontal distance (ft)')
ax1.set_ylabel('Vertical distance (ft)')
ax1.legend()
fig.savefig('single')


xft = [0,1,2,3,4,5,6,7,8,9,10]
xm = [float(x*0.3048) for x in xft]
ym = [float( h + x*np.tan(alpha)-g*(x**2)/(2*V0**2*(np.cos(alpha))**2) ) for x in xm]
yft = [float(y/0.3048) for y in ym]
for i,x in enumerate(xft):
    print('%d %0.2f' % (x,yft[i]))