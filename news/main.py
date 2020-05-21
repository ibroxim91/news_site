x = 5
g = 7
d = x + g
# print(d)

# d = [1,24,66,7,22,3,67,99,1,0,234]

# print([x for x in d if x < 50])

# v = int(input("Og'irligingiz:"))
# b = float(input("Bo'yingiz:"))
# x  =  v * v
# print(x)
# s = b / x
# print(s)

#! /usr/bin/env python
from subprocess import Popen, PIPE
import re

IP = "1.2.3.4"

pid = Popen(["arp", "-n", IP], stdout=PIPE)
id = Popen(["arp", "-n", IP], stdout=PIPE)
s = pid.communicate()[0]
mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
print(mac)


# sniff(prn=arp_monitor_callback, filter="arp", store=0)