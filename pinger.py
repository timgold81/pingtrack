#!/usr/bin/python
import sys
import os
import time
import datetime

up_interval=1
down_interval=1
#how many ping need to fail before the host declared as down
down_counter=3
if len(sys.argv)==1:
    ip_addr="8.8.8.8"
else:
    ip_addr=sys.argv[1]
status="unknown"
prev_status="unknown"


down_cnt=down_counter
while 1:
    # print ("DEBUG$$$: status: "+status+" prev_status:"+prev_status)
    res=os.system("ping -c 1 -w 1 " + ip_addr + " >/dev/null")
    if res==0:
        status="up"
        if prev_status=="unknown":
            prev_status="up"
            print ("system " + ip_addr + " up at " + str(datetime.datetime.now()))
        elif prev_status=="down":
            prev_status = "up"
            print ("system " + ip_addr + " up at " + str(datetime.datetime.now()))
        time.sleep(up_interval)
    else:
        status="down"
	if down_cnt>0:
            down_cnt=down_cnt-1
        else:
            down_cnt=down_counter
            if prev_status=="unknown":
                prev_status="down"
                print ("system " + ip_addr + " down at " + str(datetime.datetime.now()))
            elif prev_status=="up":
                prev_status="down"
                print ("system " + ip_addr + " down at " + str(datetime.datetime.now()))
        time.sleep(down_interval)



