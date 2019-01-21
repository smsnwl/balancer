

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

    def getweight0(self):

        time.sleep(1)
        #        print(h.getdv())
        k = self.getdv()
        ws00 = int(k[0]/k0)
        ws01 = int(k[1]/k1)
        ws02 = int(k[2]/k2)
        W0 = ws00 + ws01 + ws02
#        print("ws00/w01/w02",ws00,ws01,ws02,"W0",W0)
        return(ws00, ws01, ws02, W0)

    def getweight1(self):

        time.sleep(1)
        #        print(h.getdv())
        k = self.getdv()
        ws10 = int(k[0]/k0)
        ws11 = int(k[1]/k1)
        ws12 = int(k[2]/k2)
        W1 = ws10 + ws11 + ws12
        return(ws10, ws11, ws12, W1)

    
class Servo():
    def __init__(self, pin):
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
    def start(self, d):
        self.pwm.start(d)
    def change(self, d):
        self.pwm.ChangeDutyCycle(d)
    def stop(self):
        self.pwm.stop()
        
if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)                                                    
    global k0,k1,k2 ,ws00,ws01,ws02,ws10,ws11,ws12
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
    k10 = 2754
    k11 = 2916
    k12 = 2126
    j = 0
    D = []
    with open("data1.csv", "a") as datafile:
        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S\n"))
        datafile.write(", %d"%(2*R))

    S = Servo(21)
    h = SerialMeter(14, [15, 18, 23])
    time.sleep(1)
    m = h.getweight0()
    print("get_weight0", m[0], m[1], m[2],m[3])
    #        print("get_weight0", int(m[0]/k10), int(m[1]/k11), int(m[2]/k12), int(m[0]/k10 + m[1]/k11 + m[2]/k12))

    with open("data1.csv", "a") as datafile:
        datafile.write(" %d"%m[0])
        datafile.write(", %d"%m[1])
        datafile.write(", %d"%m[2])
        datafile.write(", %d\n"%m[3])

    
    for i in range(100):
        
        time.sleep(2)
        m1 = h.getweight1()                
        print("getweight1()", m1[0], m1[1], m1[2], m1[3])
 #       print("getweight1()", int(m1[0]/k10), int(m1[1]/k11), int(m1[2]/k12), int(m1[0]/k10 + m1[1]/k11 + m1[2]/k12))
 #       print("w0/w1/w2/W", int(m1[0]/k10-m[0]/k10),int(m1[1]/k10-m[1]/k10),int(m1[2]/k10-m[2]/k10),int((m1[0]/k10 + m1[1]/k11 + m1[2]/k12) - (m[0]/k10 + m[1]/k11 + m[2]/k12)))
        print("")
                
        with open("data1.csv", "a") as datafile:
            datafile.write(", %d"%i)
        
            datafile.write(", %d"%m1[0])
            datafile.write(", %d"%m1[1])
            datafile.write(", %d"%m1[2])
            datafile.write(", %d\n"%m1[3])
#            datafile.write(", %d"%W)
        i = i + 1



    GPIO.cleanup()            
