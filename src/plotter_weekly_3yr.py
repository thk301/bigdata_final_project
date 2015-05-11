############################################
#   Plots weekly trend of 3yr
#   
#   May 7, 2015
#
#   Input is hard-coded: 3 year results from reducer_weekly.py
#
############################################

import csv
import pandas as pd
from matplotlib import pyplot as plt
import sys
import ast
from datetime import datetime

if __name__ == "__main__":
    thisdata ="../data/part-00000_weekly_3yr"
    week = []
    with open(thisdata, 'r') as f:
        for line in f:
            week.append(line.strip().split('\t'))  

    newWeek={}
    for i in week:
        key=i[0]
        newWeek[key]=i[1]

    fig = plt.figure(figsize=(14,8), dpi=90)
    ax1 = plt.subplot(111)         
    ax1.plot([newWeek[i] for i in sorted(newWeek)], 'r')
    ax1.set_ylabel('Count')
    ax1.set_xlim([0,364])
    ax1.set_xticks([x*3 for x in range(0, 120)], minor = True)
    ax1.xaxis.set_tick_params(labeltop='on')
    ax1.set_xticks([x*30 for x in range(0, 12)])
    ax1.set_xticklabels(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    ax1.tick_params(axis='both',  labelsize=10)
    ax1.set_xlabel('2011, 2012, and 2013 Taxi Ride')

    ax1.annotate('WHY?', xy=(95, 950000),  xycoords='data',
                xytext=(0.35, 0.4), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )
    ax1.annotate('Labor Day', xy=(242, 800000),  xycoords='data',
                xytext=(0.7, 0.3), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )

    plt.tight_layout()
    plt.show()
