#!/usr/bin/python
import sys
import os
import time
import datetime
import argparse
import signal
import platform

def signal_handler(signal,frame):
    global loop
    loop=0
    print ("\nStopping pinger. Thanks for using.")
    print ("Please visit https://github.com/timgold81/")
    print ("contact timgold@gmail.com\n")


signal.signal(signal.SIGINT,signal_handler)

parser=argparse.ArgumentParser(description="Ping tracker of a host. Shows the time when the host went UP or DOWN")
parser.add_argument("-s","--host",help="Host name or IP address. Default = 8.8.8.8")
parser.add_argument("-d","--down",help="How many pings get lost, until the host declared as DOWN. Default=3")
parser.add_argument("-o","--down_interval",help="Interval between pings when host is down. Default=1")
parser.add_argument("-u","--up_interval",help="Interval between pings when host is up. Default=1")
args=parser.parse_args()

if args.host:
    ip_addr=args.host
else:
    ip_addr="8.8.8.8"

if args.down:
    down_counter=int(args.down)
else:
    down_counter=3

if args.down_interval:
    down_interval=float(args.down_interval)
else:
    down_interval=1

if args.up_interval:
    up_interval=float(args.up_interval)
else:
    up_interval=1

status="unknown"
prev_status="unknown"
down_cnt=down_counter
loop=1

if  platform.system()=="Windows":
    print ("Pingtracker down no operate well under Windows")
    print ("Try linux or ubuntu under Windows 10")

print ("Tracking "+ip_addr +":")

while loop:
    # print ("DEBUG$$$: status: "+status+" prev_status:"+prev_status)
    if platform.system()=="Linux":
        res=os.system("ping -c 1 -w 1 " + ip_addr + " >/dev/null")
    elif platform.system()=="Windows":
        res=os.system("ping -n 1 -w 1000 " + ip_addr + "> nul")
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
