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
    pinger.loop=0
    print ("\nStopping pinger. Thanks for using.")
    print ("Please visit https://github.com/timgold81/")
    print ("contact timgold@gmail.com\n")



class Pinger:
    status="unknown"
    prev_status="unknown"
    down_counter=3
    down_cnt=3
    down_interval=1
    up_interval=1
    loop=1
    ip_addr="8.8.8.8"


    def handle_args(self):
        parser=argparse.ArgumentParser(description="Ping tracker of a host. Shows the time when the host went UP or DOWN")
        parser.add_argument("-s","--host",help="Host name or IP address. Default = 8.8.8.8")
        parser.add_argument("-d","--down",help="How many pings get lost, until the host declared as DOWN. Default=3")
        parser.add_argument("-o","--down_interval",help="Interval between pings when host is down. Default=1")
        parser.add_argument("-u","--up_interval",help="Interval between pings when host is up. Default=1")
        args=parser.parse_args()

        if args.host:
            self.ip_addr=args.host
        else:
            self.ip_addr="8.8.8.8"

        if args.down:
            
            self.down_counter=int(args.down)
        else:
            self.down_counter=3

        if args.down_interval:
            self.down_interval=float(args.down_interval)
        else:
            self.down_interval=1

        if args.up_interval:
            self.up_interval=float(args.up_interval)
        else:
            self.up_interval=1

        self.status="unknown"
        self.prev_status="unknown"
        self.down_cnt=self.down_counter
        self.loop=1

    def start(self):
        print ("Tracking "+self.ip_addr +":")
        while self.loop:
            # print ("DEBUG$$$: status: "+status+" prev_status:"+prev_status)
            if platform.system()=="Linux":
                res=os.system("ping -c 1 -w 1 " + self.ip_addr + " >/dev/null")
            elif platform.system()=="Windows":
                res=os.system("ping -n 1 -w 1000 " + self.ip_addr + "> nul")
            if res==0:
                self.status="up"
                if self.prev_status=="unknown":
                    self.prev_status="up"
                    print ("system " + self.ip_addr + " up at " + str(datetime.datetime.now()))
                elif self.prev_status=="down":
                    self.prev_status = "up"
                    print ("system " + self.ip_addr + " up at " + str(datetime.datetime.now()))
                time.sleep(self.up_interval)
            else:
                self.status="down"
                if self.down_cnt>0:
                    self.down_cnt=self.down_cnt-1
                else:
                    self.down_cnt=self.down_counter
                    if self.prev_status=="unknown":
                        self.prev_status="down"
                        print ("system " + self.ip_addr + " down at " + str(datetime.datetime.now()))
                    elif self.prev_status=="up":
                        self.prev_status="down"
                        print ("system " + self.ip_addr + " down at " + str(datetime.datetime.now()))
                time.sleep(self.down_interval)


if __name__=="__main__":
    signal.signal(signal.SIGINT,signal_handler)
    global pinger
    pinger=Pinger()
    pinger.handle_args()
    pinger.start()