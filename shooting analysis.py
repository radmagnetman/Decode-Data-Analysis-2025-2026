import matplotlib.pyplot as plt

file = r"datalogs\\20250920 Initial shooting tests\\shooterTester_20250920-105917.csv"

timeStamp = []
setPower = []
current = []
running = []
ticks = []
velocity = []
ballShot = []

with open(file, "r",errors='ignore') as f: 
    for lineNumber, readLine in enumerate(f,1):
        if lineNumber == 1:
            continue
        readLine = readLine.rstrip()
        myList = readLine.split(",")

        timeStamp.append(float(myList[0]))
        setPower.append(float(myList[1]))
        current.append(float(myList[2]))
        if(myList[3] == 'true'):
            running.append(True)
        else:
            running.append(False)
        ticks.append(float(myList[4]))
        velocity.append(-float(myList[5]))
        if(myList[6] == 'true'):
            ballShot.append(True)
        else:
            ballShot.append(False)


fig, ax1 = plt.subplots(layout='constrained',dpi=300)
ax1.plot(timeStamp,velocity,label='Velocity')
ylim = ax1.get_ylim()
ax1.plot([13.3,13.3],ylim,'r')
ax1.plot([16.2,16.2],ylim,'r')
ax1.plot([14,14],ylim,'r--')
ax1.set_ylim(ylim[0],ylim[1])
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Velocity (ticks/sec)')
fig.savefig('time vs velocity')

fig, ax1 = plt.subplots(layout='constrained',dpi=300)
ax1.plot(timeStamp,current,label='Current')
ylim = ax1.get_ylim()
ax1.plot([13.3,13.3],ylim,'r')
ax1.plot([16.5,16.5],ylim,'r')
ax1.set_ylim(ylim[0],ylim[1])
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Current (amps)')
fig.savefig('time vs current')




# currentTransform = [c/7*1400 for c in current]
# fig, ax1 = plt.subplots(layout='constrained',dpi=300)
# ax1.plot(timeStamp,currentTransform,label='Current')
# ax1.plot(timeStamp,velocity,label='Velocity')
# ax1.set_xlabel('Time (sec)')
# ax1.set_ylabel('Current (amps)')
# ax1.legend()
# fig.savefig('time vs current and velocity')
