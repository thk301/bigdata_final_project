#!/usr/bin/python

import sys
from datetime import datetime
import time

current_key = None
current_sum = 0
daily ={}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    key, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    stringToDate = datetime.strptime(key, "%Y-%m-%d %H:%M ")
    daily_key = datetime.strftime(stringToDate, "%Y-%m-%w %H")
 
    if daily_key in daily:
        daily[daily_key] += 1
    else:
        daily[daily_key] = 1
        
for k,v in daily.items():
    print '%s\t%s' % (k, v)

