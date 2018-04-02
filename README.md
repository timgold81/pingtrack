# pingtrack<br />
<br />
usage: pinger.py [-h] [-s HOST] [-d DOWN] [-o DOWN_INTERVAL] [-u UP_INTERVAL]<br />
<br />
Ping tracker of a host. Shows the time when the host went UP or DOWN<br />
<br />
optional arguments:<br />
&nbsp;&nbsp;-h, --help            show this help message and exit<br />
&nbsp;&nbsp;-s HOST, --host HOST  Host name or IP address. Default = 8.8.8.8<br />
&nbsp;&nbsp;-d DOWN, --down DOWN  How many pings get lost, until the host declared as<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOWN. Default=3<br />
&nbsp;&nbsp;-o DOWN_INTERVAL, --down_interval DOWN_INTERVAL<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interval between pings when host is down. Default=1<br />
&nbsp;&nbsp;-u UP_INTERVAL, --up_interval UP_INTERVAL<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interval between pings when host is up. Default=1<br />
<br />
Example:<br />
tim@tim-stat:~/python/pingtrack$ ./pinger.py -s 10.0.2.31<br />
Tracking 10.0.2.31:<br />
system 10.0.2.31 up at 2018-04-02 10:37:05.976400<br />
system 10.0.2.31 down at 2018-04-02 10:37:19.039902<br />
system 10.0.2.31 up at 2018-04-02 10:37:26.063647<br />
^C<br />
Stopping pinger. Thanks for using.<br />
Please visit https://github.com/timgold81/<br />
contact timgold@gmail.com<br />
