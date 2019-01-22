
import drivers
import RPi.GPIO as GPIO
import subprocess
import time
import sys
import random
import math
from fractions import gcd

class SerialMeter:
    def __init__(self, psck, pdt):
        GPIO.setup(pdt, GPIO.IN)
        GPIO.setup(psck, GPIO.OUT, initial=0)
        self.pdt = pdt
        self.psck = psck
        
    def getdv(self, nbits=24):
        dr = [0] * len(self.pdt)
        
        for dt in self.pdt:
            while GPIO.input(dt)==1:
                pass
            
        for i in range(nbits):
            GPIO.output(self.psck, 1)
            GPIO.output(self.psck, 0)
            for (j, dt) in enumerate(self.pdt):
                dr[j] = (dr[j] << 1) | GPIO.input(dt)
                
        GPIO.output(self.psck, 1)
        GPIO.output(self.psck, 0)
            
        for j in range(len(dr)):
            if (dr[j] & (1 << (nbits - 1))) != 0:
                dr[j] = dr[j] - (1 << nbits)
                
        return dr
    
if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)                                                    
    ws00 = 0
    ws01 = 0
    ws02 = 0
    ws10 = 0
    ws11 = 0
    ws12 = 0
    ws0 = 0
    ws1 = 0
    ws2 = 0
    W0 = 0
    W1 = 0
    W = 0
    Wa = 0
    B0 = 0
    r = 183
    R = 200
    k0 = 1
    k1 = 1
    k2 = 1
    k10 = 2489
    k11 = 3048
    k12 = 2262
    j = 0
    with open("data.csv", "a") as datafile:
        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
        datafile.write(", %d"%(2*R))

    h = SerialMeter(14, [15, 18, 23])

    time.sleep(1)
    m = h.getdv()
    print("m", m[0], m[1], m[2])

    while True:
        try:

        # for i in range(3):
            time.sleep(0.05)
            m1 = h.getdv()
            w0 = (m1[0] - m[0])
            w1 = (m1[1] - m[1])
            w2 = (m1[2] - m[2])
            W = w0/k10 + w1/k11 + w2/k12

            if W > 100 and  W - Wa > 100:
                time.sleep(0.5)
                m1 = h.getdv()
                w0 = (m1[0] - m[0])
                w1 = (m1[1] - m[1])
                w2 = (m1[2] - m[2])
                W = w0/k10 + w1/k11 + w2/k12
                print("No.", j)
                print("m1", m1[1], m1[1], m1[2])
                with open("data1.csv", "a") as datafile:
                    datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
                    datafile.write(", %d"%(j*20))
                    datafile.write(", %d"%m1[0])
                    datafile.write(", %d"%m1[1])
                    datafile.write(", %d\n"%m1[2])
                    j = j + 1
            else:
                pass
            Wa = W
            
        except KeyboardInterrupt:

            GPIO.cleanup()            
