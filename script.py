#! /usr/bin/python
import subprocess
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from numpy.lib.function_base import append


IP = input("Ip Address: ")
Key = input("Key: ")



IfSpeed = subprocess.getoutput("snmpwalk -v2c -c"+" "+Key+ " " +IP+" "+ "1.3.6.1.2.1.2.2.1.5.1 | cut -c 36-43")
IfSpeed = int(IfSpeed)

ifInOctets = subprocess.getoutput("snmpwalk -v2c -c"+" "+Key+ " " +IP+" "+ "1.3.6.1.2.1.2.2.1.10.1 | cut -c 39-44")
ifInOctets = int(ifInOctets)

ifOutOctets = subprocess.getoutput("snmpwalk -v2c -c"+" "+Key+ " " +IP+" "+ "1.3.6.1.2.1.2.2.1.16.1 | cut -c 39-44")
ifOutOctets = int(ifOutOctets)


x = 100
newx = []

newyF = []
newyH = []
newyI = []
newyO = []

plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))
plt.title("Live Bandwidth Graph", fontsize=25)
plt.xlabel("Time(sec)")
plt.ylabel("Value(bit)")

ax.scatter(newx, newyF, color='blue',label ="Full-Duplex")
ax.scatter(newx, newyH, color='red',label ="Half-Duplex")
ax.scatter(newx, newyI, color='green',label ="InTraffic")
ax.scatter(newx, newyO, color='yellow',label ="OutTraffic")
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
          fancybox=True, shadow=True, ncol=5)
	

'''
FullDuplex = max((ifInOctets,ifOutOctets) * 8 * 100) / (1 * IfSpeed)
HalfDuplex = ((ifInOctets + ifOutOctets) * 8 * 100) / (1 * IfSpeed)
InTraffic = (ifInOctets * 8 * 100) / (1 * IfSpeed)
OutTraffic = (ifOutOctets * 8 * 100) / (1 * IfSpeed)
'''

for i in range(x):
    newyF.append(max((ifInOctets,ifOutOctets) * 8 * 100) / (1 * IfSpeed))
    newyH.append(((ifInOctets + ifOutOctets) * 8 * 100) / (1 * IfSpeed))
    newyI.append((ifInOctets * 8 * 100) / (1 * IfSpeed))
    newyO.append((ifOutOctets * 8 * 100) / (1 * IfSpeed))


    time.sleep(3)
    newx.append(i*3)
    line1, = ax.plot(i*3, newyF[-1], color="blue",label ="1")
    line1.set_xdata(newx)
    line1.set_ydata(newyF)
    
    line2, = ax.plot(i*3, newyH[-1], color="red",label ="2")
    line2.set_xdata(newx)
    line2.set_ydata(newyH)
        
    line3, = ax.plot(i*3, newyI[-1], color="green")
    line3.set_xdata(newx)
    line3.set_ydata(newyI)

    line4, = ax.plot(i*3, newyO[-1], color="yellow")
    line4.set_xdata(newx)
    line4.set_ydata(newyO)
    
    figure.canvas.draw()    
    figure.canvas.flush_events()
    x = +1
    plt.show()




