import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file = 'bionic-shooter-baseline\\shooterTester_20251028-165052.csv'
file = 'bionic-shooter-baseline\\shooterTester_20251028-171013.csv'


#Timestamp,Set Power,Current,Battery Voltage,Running,Ticks,Velocity,PIDF
df = pd.read_csv(file)

dfRunning = df.loc[df["Running"] == True]
t = dfRunning["Timestamp"]
velocity = dfRunning["Velocity"]
current = dfRunning["Current"]

# create running average of 10 values to smooth data.
velocityAvg = []
avgArray = [0,0,0,0,0]#,0,0,0,0,0]
for v in velocity:
    avgArray.pop()
    avgArray.insert(0, v)
    velocityAvg.append(float(np.average(avgArray)))

fig, ax1 = plt.subplots(layout='constrained',dpi=300)
#ax1.plot(t,velocity,label='Velocity',zorder = 2)
ax1.plot(t,velocityAvg,'g',zorder=3)
xlim = ax1.get_xlim()
ylim = ax1.get_ylim()
ax1.plot(xlim,[1200,1200],'r',zorder = 1)
ax1.plot([186,186],[900,1400],'r',zorder = 1)
ax1.plot([186.4,186.4],[900,1400],'r',zorder = 1)
ax1.plot([186.9,186.9],[900,1400],'r',zorder = 1)
#print(float(471.5-t.iloc[0]))
#ax1.set_ylim(ylim[0],ylim[1])
ax1.set_ylim(900,1400)
ax1.set_xlim(180,200)
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Velocity (ticks/sec)')
fig.savefig('baseline - time vs velocity 1')

fig, ax1 = plt.subplots(layout='constrained',dpi=300)
#ax1.plot(t,velocity,label='Velocity',zorder = 2)
ax1.plot(t,current,'g',zorder=3)
xlim = ax1.get_xlim()
ylim = ax1.get_ylim()
#ax1.plot(xlim,[1200,1200],'r',zorder = 1)
#ax1.plot([186,186],[0,6],'r',zorder = 1)
#ax1.plot([186.4,186.4],[0,6],'r',zorder = 1)
#ax1.plot([186.9,186.9],[0,6],'r',zorder = 1)
#print(float(471.5-t.iloc[0]))
#ax1.set_ylim(ylim[0],ylim[1])
#ax1.set_ylim(900,1400)
#ax1.set_xlim(180,200)
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Current (amps)')
fig.savefig('baseline - time vs current 1')



fig, ax1 = plt.subplots(layout='constrained',dpi=300)
#ax1.plot(t,velocity,label='Velocity',zorder = 2)
ax1.plot(t,velocityAvg,'g',zorder=3)
xlim = ax1.get_xlim()
ylim = ax1.get_ylim()
ax1.plot(xlim,[1200,1200],'r',zorder = 1)
ax1.plot([237,237],[900,1400],'r',zorder = 1)
ax1.plot([237.3,237.3],[900,1400],'r',zorder = 1)
ax1.plot([237.9,237.9],[900,1400],'r',zorder = 1)
#print(float(471.5-t.iloc[0]))
ax1.set_ylim(ylim[0],ylim[1])
ax1.set_ylim(900,1400)
ax1.set_xlim(225,245)
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Velocity (ticks/sec)')
fig.savefig('baseline - time vs velocity 2')

