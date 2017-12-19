#!/usr/bin/python
import sys
import os
import time
import datetime

up_interval=3
down_interval=1
if len(sys.argv)==1:
    ip_addr="192.168.0.199"
else:
    ip_addr=sys.argv[1]
status="unknown"
prev_status="unknown"

while 1:
    # print ("DEBUG$$$: status: "+status+" prev_status:"+prev_status)
    res=os.system("ping -c 1 -w 1 " + ip_addr + " >/dev/null")
    if res==0:
        time.sleep(up_interval)
        status="up"
        if prev_status=="unknown":
            prev_status="up"
            print ("system " + ip_addr + " up at " + str(datetime.datetime.now()))
        elif prev_status=="down":
            prev_status = "up"
            print ("system " + ip_addr + " up at " + str(datetime.datetime.now()))
    else:
        time.sleep(down_interval)
        status="down"
        if prev_status=="unknown":
            prev_status="down"
            print ("system " + ip_addr + " down at " + str(datetime.datetime.now()))
        elif prev_status=="up":
            prev_status="down"
            print ("system " + ip_addr + " down at " + str(datetime.datetime.now()))



