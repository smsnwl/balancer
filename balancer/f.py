
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
#        print("ws00",ws00,"W0",W0)
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
    k0 = 2623
    k1 = 2833
    k2 = 2198
    h = SerialMeter(14, [15, 18, 23])

    time.sleep(1)
    m = h.getweight0()
    print("get_weight0", m[0], m[1], m[2],m[3])


    while True:
        try:
            for i in range(3):
                time.sleep(0.5)
                m1 = h.getweight1()                
                print("1", h.getweight1())
                w0 = (m1[0] - m[0])
                w1 = (m1[1] - m[1])
                w2 = (m1[2] - m[2])
                W = (m1[3] - m[3])
                print("W", W)
                if W < 20:
                    i = i
                else:
                    x0 = (1.5*w0/W-0.5)*r
                    y0 = r-3*r*w1/W-x0
                    # y0 = r+3*r*w1/W-x0
                    d = math.sqrt(x0*x0 + y0*y0)
                    g = d*W/R
                    
                    if x0 == 0 and y0 == 0:
                        B0 = 0
                        print("0")
                    elif x0 == 0 and y0 > 0:
                        B0 = math.pi/2
                    elif x0 == 0 and y0 < 0:
                        B0 = 1.5*math.pi
                    elif x0 > 0 and y0 >= 0:
                        B0 = math.atan(y0/x0)
                    elif x0 > 0 and y0 < 0:
                        B0 = 2*math.pi+math.atan(y0/x0)
                    elif x0 < 0 and y0 >=0:
                        B0 = math.pi + math.atan(y0/x0)
                    elif x0 <0 and y < 0:
                        B0 = math.pi + math.atan(y0/x0)
                    else:
                        pass
                    print("g= ", int(g*100)/100, "B0=  ", int(B0*10000)/10000, "d=", int(d*100)/100,  "x0=", int(x0*100)/100, "y0=", int(y0*100)/100 )
                    print("")

                    with open("data.csv", "a") as datafile:
                        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
                        datafile.write(", %d"%i)
                        datafile.write(", %d"%R)
                        datafile.write(", %d"%W)
                        datafile.write(", %d"%g)
                        datafile.write(", %d"%B0)
                        datafile.write(", %d"%d)
                        datafile.write(", %d"%x0)
                        datafile.write(", %d"%y0)

                i = i + 1
        except KeyboardInterrupt:

            GPIO.cleanup()            
