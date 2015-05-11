############################################
#   Plots daily trend of 3 Years
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
    thisdata = "../data/part-00000_daily_3yr"
    day = []
    with open(thisdata, 'r') as f:
        for line in f:
            day.append(line.strip().split('\t'))
            
   
    newDay = {}
    for i in day:
        key = i[0]
        newDay[key] = i[1]
    
    oneYear = {}
    for k, v in sorted(newDay.iteritems())[0:24 * 7 * 12]:
          time = k[8:]
          if time in oneYear:
              oneYear[time] += int(v)
          else:
              oneYear[time] = int(v)
              
    twoYear = {}
    for k, v in sorted(newDay.iteritems())[24 * 7 * 12:24 * 7 * 24]:
          time = k[8:]
          if time in twoYear:
              twoYear[time] += int(v)
          else:
              twoYear[time] = int(v)

    threeYear = {}
    for k, v in sorted(newDay.iteritems())[24 * 7 * 24:24 * 7 * 36]:
          time = k[8:]
          if time in threeYear:
              threeYear[time] += int(v)
          else:
              threeYear[time] = int(v)         
   
              
    fig = plt.figure(figsize=(14, 8), dpi=90)
    ax1 = plt.subplot(111)         
    ax1.plot([oneYear[i] for i in sorted(oneYear)], '#a6d96a', label='2011')
    ax1.plot([twoYear[i] for i in sorted(twoYear)], '#2c7bb6', label='2012')
    ax1.plot([threeYear[i] for i in sorted(threeYear)], '#f03b20' , label='2013')
    legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    ax1.xaxis.set_tick_params(labeltop='on')
    ax1.set_xlabel('2011, 2012, 2013 Taxi Ride - by Different Years')
    ax1.set_ylabel('Count')
    ax1.set_xlim([0, 24 * 7])
    ax1.set_xticks([x * 3 for x in range(0, 8 * 7)], minor=True)
    ax1.set_xticklabels([x * 3 for x in range (0, 8)], minor=True, size=8)  
    ax1.set_xticks([24 * x for x in range(0, 7)])
    ax1.set_xticklabels(['Sunday', 'Monday', 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' ])
    ax1.tick_params(axis='both', labelsize=10)
    plt.tight_layout()
    plt.show()

     
