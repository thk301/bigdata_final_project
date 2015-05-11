#!/usr/bin/python

import sys
from datetime import datetime
import time

current_key = None
current_sum = 0
weekly ={}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    key, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    stringToDate = datetime.strptime(key, "%Y-%m-%d %H:%M ")
    weekly_key = datetime.strftime(stringToDate, "%U-%w")
 
    if weekly_key in weekly:
        weekly[weekly_key] += 1
    else:
        weekly[weekly_key] = 1
    
for k,v in weekly.items():
      print '%s\t%s' % (k, v)

