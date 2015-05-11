#!/usr/bin/python

import sys
import string
import os
import re
from datetime import datetime
import time

def mapper():
 '''
 map function to get pickup_datetime
 '''
 # input comes from STDIN (stream data that goes to the program)
 for line in sys.stdin:
    line = line.strip()
    seperate_line = line.split(",")
    if len(seperate_line) ==14: 
        medallion, hack_license, vendor_id, rate_code,store_and_fwd_flag,pickup_datetime, dropoff_datetime, \
        passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, \
        dropoff_longitude, dropoff_latitude =seperate_line

        if medallion!="medallion":
            stringToDate = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
            key = datetime.strftime(stringToDate, "%Y-%m-%d %H:%M")
            value = 1
            print "%s \t %s" %(key, value)
    else:
        pass
        
if __name__=='__main__':
    mapper()
