import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import glob

# relevant info to pull files. First line is the timestamp for the file name,
# second line is the indexes in the individual files to plot, third line is label
# to help identify on graph
lookingAt = ['151929','152542','154040']
timeBox = [[187.1,210],[36,45],[66.9,72]]
desc = ['30','40','50']

# get all csv files
dataPath = 'bionic-shooter-pid-tuning\\'
os.chdir(dataPath)
files = glob.glob('*.csv')

fileName = ''

fig, ax1 = plt.subplots(2)

# for each file name, find file
for i, f in enumerate(lookingAt):
    for s in files:
        if f in s: 
            fileName = s
            break

    print('Reading %s' % (fileName))
    
    # Read file
    df = pd.read_csv(fileName)
    fname = fileName.split('.')
    fname = fname[0]

    # reduce data set to 'running' and inside time bounds
    dfRunning = df.loc[(df["Running"] == True) & (df["Timestamp"] > timeBox[i][0]) & (df["Timestamp"] < timeBox[i][1])]
    t = dfRunning["Timestamp"]
    t0 = float(t.iloc[0])
    tplt = []
    for j in range(t.shape[0]):
        tplt.append( float(t.iloc[j] - t0))
    velocity = dfRunning["Velocity"]
    current = dfRunning["Current"]

    # plot
    ax1[0].plot(tplt, velocity,label=desc[i])
    ax1[1].plot(tplt, current)

fig.suptitle('target 1200 ticks/rev')
ax1[0].set_ylabel('Velocity')
ax1[0].legend()
ax1[1].set_ylabel('Current')
ax1[1].set_xlabel('Time (sec)')
ax1[0].set_xlim(0,5)
ax1[1].set_xlim(0,5)
fig.savefig('target_1200_all_time')
