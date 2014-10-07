#!/usr/bin/python

from si import *

s1 = Si7005()

print "Hum:  %.2f Temp: %.2f" % (s1.readHumidity(), s1.readTemperature())

#other method, faster if both data is needed:
print "Hum:  %.2f Temp: %.2f"  % s1.readHumidityTemperature()

# short methods:
print "Hum:  %.2f Temp: %.2f" % (s1.getH() , s1.getT())
print "Hum:  %.2f Temp: %.2f" % s1.getHT()


