############################################
#   Plots histogram of 3 yr counts
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
            
   
    newDay = {}
    for i in day:
        key = i[0]
        newDay[key] = i[1]
    
    thisYear = {}
    for k, v in sorted(newDay.iteritems())[0:24 * 7 * 12]:
          time = k[:4]
          if time in thisYear:
              thisYear[time] += int(v)
          else:
              thisYear[time] = int(v)
              
    for k, v in sorted(newDay.iteritems())[24 * 7 * 12:24 * 7 * 24]:
          time = k[:4]
          if time in thisYear:
              thisYear[time] += int(v)
          else:
              thisYear[time] = int(v)

    for k, v in sorted(newDay.iteritems())[24 * 7 * 24:24 * 7 * 36]:
          time = k[:4]
          if time in thisYear:
              thisYear[time] += int(v)
          else:
              thisYear[time] = int(v)       
    #plotNum = thisYear.values()
    #print plotNum
   
    fig = plt.figure(figsize=(14, 8), dpi=90)
    ax1 = plt.subplot(111)         
    
    plt.bar(xrange(len(thisYear)), [v for k,v in sorted(thisYear.iteritems())], width=0.3, color=['#a6d96a','#2c7bb6','#f03b20'], align='center')
    ax1.set_ylim([140000000, 180000000])
    ax1.set_ylabel('Total Count')
    ax1.set_xticks([x * 1 for x in range(0, 3)])
    ax1.set_xticklabels(['2011' , '2012' , '2013' ])
    ax1.tick_params(axis='both', labelsize=10)
    ax1.set_xlabel('2011, 2012, 2013 Taxi Ride - Overall Counts')
    
    ax1.annotate(thisYear["2011"], xy=(0, thisYear["2011"]),  xycoords='data',
                  xytext=(0.1, 0.8), textcoords='axes fraction',
                  arrowprops=dict(facecolor='black', shrink=0.05),
                  horizontalalignment='right', verticalalignment='top',
                  )
    ax1.annotate(thisYear["2012"], xy=(1, thisYear["2012"]),  xycoords='data',
                  xytext=(0.4, 0.8), textcoords='axes fraction',
                  arrowprops=dict(facecolor='black', shrink=0.05),
                  horizontalalignment='right', verticalalignment='top',
                  )
    ax1.annotate(thisYear["2013"], xy=(2, thisYear["2013"]),  xycoords='data',
                  xytext=(0.75, 0.8), textcoords='axes fraction',
                  arrowprops=dict(facecolor='black', shrink=0.05),
                  horizontalalignment='right', verticalalignment='top',
                  )
    plt.tight_layout()
    plt.show()
        
 
     
     
      