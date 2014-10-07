#!/usr/bin/python

from si import *

s1 = Si7005()

print "Hum:  %.2f" % s1.readHumidity()
print "Temp: %.2f" % s1.readTemperature()

#other method, faster if both data is needed:
(h1,t1) =s1.readHumidityTemperature()
print "Hum:  %.2f" % h1
print "Temp: %.2f" % t1

# short methods:
print "Hum:  %.2f" % s1.getH()
print "Temp: %.2f" % s1.getT()
print "Hum:  %.2f Temp: %.2f" % s1.getHT()


