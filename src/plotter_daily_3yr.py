############################################
#   Plots overall trend of 3yr year (by daily) 
#   
#   May 7, 2015
#
#   Input is hard-coded: 3 year results from reducer_daily.py
#
############################################


import csv
import pandas as pd
from matplotlib import pyplot as plt
import ast
from datetime import datetime
import numpy as np
   
if __name__ == "__main__":
    thisdata ="../data/part-00000_daily_3yr"
    day = []
    with open(thisdata, 'r') as f:
        for line in f:
            day.append(line.strip().split('\t'))
            

    newDay={}
    for i in day:
        key=i[0]
        newDay[key]=i[1]
    
    fig = plt.figure(figsize=(14,8), dpi=90)
    ax1 = plt.subplot(111)         
    ax1.plot([newDay[i] for i in sorted(newDay)], 'b-')
    ax1.set_ylabel('Count')
    ax1.set_xlim([0,24*7*12*3])
    ax1.set_xticks([24*7*x for x in range(0, 12*3)], minor = True)
    ax1.xaxis.set_tick_params(labeltop='on')
    ax1.set_xticklabels(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], minor = True, rotation='vertical', size=8)
    ax1.set_xticks([24*7*12*x for x in range(0, 4)])
    ax1.set_xticklabels(["2011", "2012", "2013"])
    ax1.tick_params(axis='both',  labelsize=10)
    ax1.set_xlabel('2011, 2012, 2013 Taxi Ride')
    ax1.annotate('2011 North American heat wave ', xy=(30*7*5+150, 54000),  xycoords='data',
                xytext=(0.3, 0.05), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )
    plt.tight_layout()
    plt.show()
    
    
     