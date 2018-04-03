# pingtrack
Use ping to log the time when a host went up or down
<pre>
usage: pinger.py [-h] [-s HOST] [-d DOWN] [-o DOWN_INTERVAL] [-u UP_INTERVAL]

Ping tracker of a host. Shows the time when the host went UP or DOWN

optional arguments:
  -h, --help            show this help message and exit
  -s HOST, --host HOST  Host name or IP address. Default = 8.8.8.8
  -d DOWN, --down DOWN  How many pings get lost, until the host declared as
                        DOWN. Default=3
  -o DOWN_INTERVAL, --down_interval DOWN_INTERVAL
                        Interval between pings when host is down. Default=1
  -u UP_INTERVAL, --up_interval UP_INTERVAL
                        Interval between pings when host is up. Default=1
</pre>

# Example:<br />
<pre>
tim@tim-stat:~/python/pingtrack$ ./pinger.py -s 10.0.2.31
Tracking 10.0.2.31:
system 10.0.2.31 up at 2018-04-02 10:37:05.976400
system 10.0.2.31 down at 2018-04-02 10:37:19.039902
system 10.0.2.31 up at 2018-04-02 10:37:26.063647
ctrl+C
Stopping pinger. Thanks for using.
Please visit https://github.com/timgold81/
contact timgold@gmail.com
</pre>
