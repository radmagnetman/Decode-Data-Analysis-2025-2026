import matplotlib.pyplot as plt
import sys
import os

folder = "Datalogs"

for filename in os.listdir(folder):
    if(not filename.endswith(".csv")):
        continue;

    file = os.path.join(folder, filename)
    print(file)

    timeStamp = []
    setPower = []
    current = []
    voltage = []
    ticks = []
    velocity = []

    with open(file, "r",errors='ignore') as f:
        for lineNumber, readLine in enumerate(f,1):
            if lineNumber == 1:
                continue
            readLine = readLine.rstrip()
            myList = readLine.split(",")

            timeStamp.append(float(myList[0]))
            setPower.append(float(myList[1]))
            current.append(float(myList[2]))
            voltage.append(float(myList[3]))
            ticks.append(float(myList[5]))
            velocity.append(-float(myList[6]))

    # for the filename
    digits = filename.split("-")[1].split(".")[0]

    fig, ax1 = plt.subplots(layout='constrained',dpi=300)
    ax1.plot(timeStamp,velocity,label='Velocity')
    ylim = ax1.get_ylim()
    ax1.set_ylim(ylim[0],ylim[1])
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Velocity (ticks/sec)')
    fig.savefig(f"output/time_velocity_{digits}_{abs(setPower[0]):.2f}.png")
    plt.close(fig)

    fig, ax1 = plt.subplots(layout='constrained',dpi=300)
    ax1.plot(timeStamp,current,label='Current')
    ylim = ax1.get_ylim()
    ax1.set_ylim(ylim[0],ylim[1])
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Current (amps)')
    fig.savefig(f"output/time_current_{digits}_{abs(setPower[0]):.2f}.png")
    plt.close(fig)
