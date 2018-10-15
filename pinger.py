#!/usr/bin/python
import sys
import os
import time
import datetime
import argparse
import signal
import platform

def signal_handler(signal,frame):
    # global conf
    conf.loop=0
    print ("\nStopping pinger. Thanks for using.")
    print ("Please visit https://github.com/timgold81/")
    print ("contact timgold@gmail.com\n")



class configuration:
    status="unknown"
    prev_status="unknown"
    down_counter=1
    down_cnt=0
    down_interval=0
    up_interval=0
    loop=1
    ip_addr=""


def handle_args():
    parser=argparse.ArgumentParser(description="Ping tracker of a host. Shows the time when the host went UP or DOWN")
    parser.add_argument("-s","--host",help="Host name or IP address. Default = 8.8.8.8")
    parser.add_argument("-d","--down",help="How many pings get lost, until the host declared as DOWN. Default=3")
    parser.add_argument("-o","--down_interval",help="Interval between pings when host is down. Default=1")
    parser.add_argument("-u","--up_interval",help="Interval between pings when host is up. Default=1")
    args=parser.parse_args()

    if args.host:
        conf.ip_addr=args.host
    else:
        conf.ip_addr="8.8.8.8"

    if args.down:
        
        conf.down_counter=int(args.down)
    else:
        conf.down_counter=3

    if args.down_interval:
        conf.down_interval=float(args.down_interval)
    else:
        conf.down_interval=1

    if args.up_interval:
        conf.up_interval=float(args.up_interval)
    else:
        conf.up_interval=1

    conf.status="unknown"
    conf.prev_status="unknown"
    conf.down_cnt=conf.down_counter
    conf.loop=1

def main():
    print ("Tracking "+conf.ip_addr +":")
    while conf.loop:
        # print ("DEBUG$$$: status: "+status+" prev_status:"+prev_status)
        if platform.system()=="Linux":
            res=os.system("ping -c 1 -w 1 " + conf.ip_addr + " >/dev/null")
        elif platform.system()=="Windows":
            res=os.system("ping -n 1 -w 1000 " + conf.ip_addr + "> nul")
        if res==0:
            conf.status="up"
            if conf.prev_status=="unknown":
                conf.prev_status="up"
                print ("system " + conf.ip_addr + " up at " + str(datetime.datetime.now()))
            elif conf.prev_status=="down":
                conf.prev_status = "up"
                print ("system " + conf.ip_addr + " up at " + str(datetime.datetime.now()))
            time.sleep(conf.up_interval)
        else:
            conf.status="down"
            if conf.down_cnt>0:
                conf.down_cnt=conf.down_cnt-1
            else:
                conf.down_cnt=conf.down_counter
                if conf.prev_status=="unknown":
                    conf.prev_status="down"
                    print ("system " + conf.ip_addr + " down at " + str(datetime.datetime.now()))
                elif conf.prev_status=="up":
                    conf.prev_status="down"
                    print ("system " + conf.ip_addr + " down at " + str(datetime.datetime.now()))
            time.sleep(conf.down_interval)


if __name__=="__main__":
    signal.signal(signal.SIGINT,signal_handler)
    global conf
    conf=configuration()
    handle_args()
    main()