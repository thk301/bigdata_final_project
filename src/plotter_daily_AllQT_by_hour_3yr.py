############################################
#   Plots daily trend of 4 different QTs
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
    
    oneQT={}
    for k,v in sorted(newDay.iteritems())[0:24*7*3]+sorted(newDay.iteritems())[24*7*12:24*7*15]+sorted(newDay.iteritems())[24*7*24:24*7*27]:
          time = k[8:]
          if time in oneQT:
              oneQT[time]+=int(v)
          else:
              oneQT[time]=int(v)
              
    twoQT={}
    for k,v in sorted(newDay.iteritems())[24*7*3:24*7*6]+sorted(newDay.iteritems())[24*7*15:24*7*18]+sorted(newDay.iteritems())[24*7*27:24*7*30]:
          time = k[8:]
          if time in twoQT:
              twoQT[time]+=int(v)
          else:
              twoQT[time]=int(v)

    threeQT={}
    for k,v in sorted(newDay.iteritems())[24*7*6:24*7*9]+sorted(newDay.iteritems())[24*7*18:24*7*21]+sorted(newDay.iteritems())[24*7*30:24*7*33]:
          time = k[8:]
          if time in threeQT:
              threeQT[time]+=int(v)
          else:
              threeQT[time]=int(v)         
              
    fourQT={}
    for k,v in sorted(newDay.iteritems())[24*7*9:24*7*12]+sorted(newDay.iteritems())[24*7*21:24*7*24]+sorted(newDay.iteritems())[24*7*33:24*7*36]:
          time = k[8:]
          if time in fourQT:
              fourQT[time]+=int(v)
          else:
              fourQT[time]=int(v)       
              
    fig = plt.figure(figsize=(14,8), dpi=90)
    ax1 = plt.subplot(111)         
    ax1.plot([oneQT[i] for i in sorted(oneQT)], '#d7191c', label='1st QT')
    ax1.plot([twoQT[i] for i in sorted(twoQT)], '#fdae61', label='2nd QT')
    ax1.plot([threeQT[i] for i in sorted(threeQT)], '#404040' , label='3rd QT')
    ax1.plot([fourQT[i] for i in sorted(fourQT)], '#2b83ba', label='4th QT')
    legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    ax1.xaxis.set_tick_params(labeltop='on')
    ax1.set_xlabel('2011, 2012, 2013 Taxi Ride - by Different QTs')
    ax1.set_ylabel('Count')
    ax1.set_xlim([0,24*7])
    ax1.set_xticks([x*3 for x in range(0, 8*7)], minor = True)
    ax1.set_xticklabels([x*3 for x in range (0,8)], minor = True, size=8)  
    ax1.set_xticks([24*x for x in range(0, 7)])
    ax1.set_xticklabels(['Sunday','Monday', 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' ])
    ax1.tick_params(axis='both',  labelsize=10)
    plt.tight_layout()
    plt.show()
       
     
      