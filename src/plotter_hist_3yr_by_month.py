############################################
#   Plots histogram of 3 year data by months
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
import matplotlib.patches as mpatches
   
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
           time = k[:7]
           if time in thisYear:
               thisYear[time] += int(v)
           else:
               thisYear[time] = int(v)
               
    for k, v in sorted(newDay.iteritems())[24 * 7 * 12:24 * 7 * 24]:
           time = k[:7]
           if time in thisYear:
               thisYear[time] += int(v)
           else:
               thisYear[time] = int(v)
 
    for k, v in sorted(newDay.iteritems())[24 * 7 * 24:24 * 7 * 36]:
           time = k[:7]
           if time in thisYear:
               thisYear[time] += int(v)
           else:
               thisYear[time] = int(v)  
    
    fig = plt.figure(figsize=(14, 8), dpi=90)
    ax1 = plt.subplot(111)  
    newL =[]
    for i in xrange(12): 
        for k,v in sorted(thisYear.iteritems())[i::12]:
           print k,v
           newL.append(v)
    
    plt.bar(xrange(36), [i for i in newL], width=0.7, color=['#a6d96a','#2c7bb6','#f03b20'], align='center')
  
    three_patch = mpatches.Patch(color='#f03b20', label='2013')
    two_patch = mpatches.Patch(color='#2c7bb6', label='2012')
    one_patch = mpatches.Patch(color='#a6d96a', label='2011')
    plt.legend(handles=[three_patch, two_patch, one_patch])
    ax1.set_xlim([-.2, 35.2])
    ax1.set_ylim([10000000, 16500000])
    ax1.set_ylabel('Total Count')
    ax1.set_xticks([x*3  for x in range(0, 12)])
    ax1.set_xticklabels(['January' ,'February','March', 'April' ,'May', 'June' ,'July', 'August','September', 'October' , 'November', 'December'])
    for i, j in enumerate(newL):
        ax1.annotate(j, (i,j), xytext=(0.4,.15), 
                         textcoords='offset points',rotation=90, size=12)
    ax1.set_xlabel('2011, 2012, 2013 Taxi Ride - Overall Counts per Month')
     

    plt.tight_layout()
    plt.show()
