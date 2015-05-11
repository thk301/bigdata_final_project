############################################
#   Plots weekly trend of 2013
#   
#   May 7, 2015
#
#   Input is hard-coded: 1 year results from reducer_weekly.py
#
#
############################################

import csv
import pandas as pd
from matplotlib import pyplot as plt
import sys
import ast
from datetime import datetime

if __name__ == "__main__":
    thisdata ="../data/part-00000_weekly_1yr"
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
    ax1.set_xlabel('2013 Taxi Ride')
    ax1.annotate('Warmest Weather in Months', xy=(13*7+5, 240000),  xycoords='data',
                xytext=(0.15, 0.3), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )
    ax1.annotate('2013 Heat Wave', xy=(180, 300000),  xycoords='data',
                xytext=(0.55, 0.4), textcoords='axes fraction',
                horizontalalignment='right', verticalalignment='top',
                )
    ax1.annotate('10-Day Raining and Thunderstrom', xy=(215, 195000),  xycoords='data',
                xytext=(0.55, 0.2), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )
    ax1.annotate('New York Dominican Day Parade', xy=(222, 220000),  xycoords='data',
                xytext=(0.6, 0.3), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )

    ax1.annotate('Various Events including NYC Oktoberfest', xy=(275, 220000),  xycoords='data',
                xytext=(0.9, 0.3), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )

    plt.tight_layout()
    plt.show()
