#!/usr/bin/python
import sys
import os
import time
import datetime
import argparse
import signal
import platform
import subprocess

class Pinger:
    def __init__(self):
        self.status = "unknown"
        self.prev_status = "unknown"
        self.down_counter = 3
        self.down_cnt = 3
        self.down_interval = 1
        self.up_interval = 1
        self.loop = 1
        self.ip_addr = "8.8.8.8"

    def signal_handler(self, signal, frame):
        self.loop = 0
        print("\nStopping pinger. Thanks for using.")
        print("Please visit https://github.com/timgold81/")
        print("contact timgold@gmail.com\n")

    def handle_args(self):
        parser = argparse.ArgumentParser(description="Ping tracker of a host. Shows the time when the host went UP or DOWN")
        parser.add_argument("-s", "--host", default="8.8.8.8", help="Host name or IP address.")
        parser.add_argument("-d", "--down", default=3, type=int, help="How many pings get lost, until the host declared as DOWN.")
        parser.add_argument("-o", "--down_interval", default=1, type=float, help="Interval between pings when host is down.")
        parser.add_argument("-u", "--up_interval", default=1, type=float, help="Interval between pings when host is up.")
        args = parser.parse_args()

        self.ip_addr = args.host
        self.down_counter = args.down
        self.down_interval = args.down_interval
        self.up_interval = args.up_interval
        self.down_cnt = self.down_counter

    def print_status(self, status):
        if self.prev_status != status:
            self.prev_status = status
            print("system " + self.ip_addr + " " + status + " at " + str(datetime.datetime.now()))

    def start(self):
        print("Tracking " + self.ip_addr + ":")
        while self.loop:
            if platform.system() == "Linux":
                res = subprocess.call(["ping", "-c", "1", "-w", "1", self.ip_addr], stdout=subprocess.DEVNULL)
            elif platform.system() == "Windows":
                res = subprocess.call(["ping", "-n", "1", "-w", "1000", self.ip_addr], stdout=subprocess.DEVNULL, shell=True)
            if res == 0:
                self.status = "up"
                self.print_status(self.status)
                time.sleep(self.up_interval)
            else:
                self.status = "down"
                if self.down_cnt > 0:
                    self.down_cnt -= 1
                else:
                    self.down_cnt = self.down_counter
                    self.print_status(self.status)
                time.sleep(self.down_interval)


if __name__ == "__main__":
    pinger = Pinger()
    signal.signal(signal.SIGINT, pinger.signal_handler)
    pinger.handle_args()
    pinger.start()

