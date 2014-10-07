#!/usr/bin/python
from si import *


s1 = Si7005()

while True:
    print "Hum:  %.2f Temp: %.2f" % s1.getHT()
    time.sleep(1)
