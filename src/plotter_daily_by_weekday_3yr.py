############################################
#   Plots daily trend of three year
#   
#   May 7, 2015
#
#   Input is hard-coded: 3 year results from reducer_daily.py
#
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
    
    weekDay={}
    for k,v in sorted(newDay.iteritems()):
          time = k[8:]
          if time in weekDay:
              weekDay[time]+=int(v)
          else:
              weekDay[time]=int(v)
          
    
    fig = plt.figure(figsize=(14,8), dpi=90)
    ax1 = plt.subplot(111)         
    ax1.plot([weekDay[i] for i in sorted(weekDay)], 'r')
    ax1.set_ylabel('Count')
    ax1.set_xlim([0,24*7])
    ax1.set_xticks([x*3 for x in range(0, 8*7)], minor = True)
    ax1.xaxis.set_tick_params(labeltop='on')
    ax1.set_xticklabels([x*3 for x in range (0,8)], minor = True, size=8)
    
    ax1.set_xticks([24*x for x in range(0, 7)])
    ax1.set_xticklabels(['Sunday','Monday', 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday'])
    ax1.tick_params(axis='both',  labelsize=10)
    ax1.set_xlabel('2011,2012,2013 Taxi Ride - By Weekday')
    ax1.annotate('Thursday Evening', xy=(24*4.8, 5000000),  xycoords='data',
                xytext=(0.65, 0.8), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )
    ax1.annotate('Friday Evening', xy=(24*5.8, 5000000),  xycoords='data',
                xytext=(0.85, 0.8), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
                )

    plt.tight_layout()
    plt.show()
     
