!/usr/bin/env python
import serial
import pynmea2
import datetime

serialStream = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

while True:
    sentence = serialStream.readline()
    if sentence.find('GGA') > 0:
        data = pynmea2.parse(sentence)
        print now.isoformat(),"LAT: {lat}, LON: {lon}, ALT: {alt},{alt_units}".format(time=data.timestamp,lat=data.latitude,lon=data.longitude,alt=data.altitude,alt_units=data.altitude_units)
