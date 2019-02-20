

import drivers
import RPi.GPIO as GPIO
import subprocess
import time
import sys
import random
import math
from fractions import gcd

class HX711:
    def __init__(self, psck, pdt):
        GPIO.setup(psck, GPIO.OUT, initial = 0)
        GPIO.setup(pdt, GPIO.IN)
        self.psck = psck
        self.pdt = pdt
        
    def read(self):
        d = 0
        while GPIO.input(self.pdt)==1:
            pass
        for i in range(24):
            GPIO.output(self.psck, 1)
            GPIO.output(self.psck, 0)
            d = (d << 1) | GPIO.input(self.pdt)
            #GPIO.output(psck, 0)
        GPIO.output(self.psck, 1)
        GPIO.output(self.psck, 0)
        return d
    
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
    global m00, m01, m02, k0, k1, k2

    m00 = 0
    m01 = 0
    m02 = 0
    m10 = 0
    m11 = 0
    m12 = 0
    W0 = 0
    W1 = 0
    W = 0
    Wa = 0
    B0 = 0
    r = 183
    R = 200
    k0 = 0
    k1 = 0
    k2 = 0
    j = 0

    tr = Servo(20)
    t = 0.1
    # for i in range(1):
    #     time.sleep(t)
    #     tr.start(3)
    #     print("tr", 10)
    #     tr.change(5)
    #     time.sleep(t)
    #     i = i+1
    h0 = HX711(24, 23)
    h1 = HX711(16, 12)
    h2 = HX711(21, 20)


    print("请等待5秒")
    time.sleep(5)
    m00 = h0.read()
    m01 = h1.read()
    m02 = h2.read()

    print("请放置896.4g标准盘。（5秒内）")
    time.sleep(5)
    m10 = h0.read()
    m11 = h1.read()
    m12 = h2.read()

    k0 = m10 / m00
    k1 = m11 / m01
    k2 = m12 / m02
    print(m00, m01, m02, m10, m11, m12)
    print(k0, k1, k2)
    
    print("请在10s内取走标准盘!  (5秒内)")
    time.sleep(5)
    print("可以测试样品了")
    while True:
        try:
            time.sleep(1)
            m0 = h0.read()
            m1 = h1.read()
            m2 = h2.read()
            
            w0 = (m0 - m00)
            w1 = (m1 - m01)
            w2 = (m2 - m02)
            W = w0/k0 + w1/k1 + w2/k2

            if W > 10 and  W - Wa > 10:
                time.sleep(0.5)
                for i in range(1):
#                    tr.start(3)
                    time.sleep(0.5)

                    m0 = h0.read()
                    m1 = h1.read()
                    m2 = h2.read()
                    
                    w0 = (m0 - m00)
                    w1 = (m1 - m01)
                    w2 = (m2 - m02)
                    W = w0/k0 + w1/k1 + w2/k2


                    x0 = (1.5*w0/k0/W-0.5)*r
                    y0 = r-3*r*w1/k1/W-x0
                    # y0 = r+3*r*w1/W-x0
                    d = math.sqrt(x0*x0 + y0*y0)
                    g = d*W/R
                    
                    if x0 == 0 and y0 == 0:
                        B0 = 0
                        B1 = B0
                    elif x0 == 0 and y0 > 0:
                        B0 = math.pi/2
                        B1 = B0
                    elif x0 == 0 and y0 < 0:
                        B0 = 1.5*math.pi
                        B1 = math.pi/2
                    elif x0 > 0 and y0 >= 0:
                        B0 = math.atan(y0/x0)
                        B1 = B0
                    elif x0 > 0 and y0 < 0:
                        B0 = 2*math.pi-math.atan(y0/x0)
                        B1 = math.pi-math.atan(y0/x0)
                    elif x0 < 0 and y0 >=0:
                        B0 = math.pi + math.atan(y0/x0)
                        B1 = B0 
                    elif x0 <0 and y0 < 0:
                        B0 = math.pi - math.atan(y0/x0)
                        B1 = math.atan(y0/x0)
                    else:
                        pass
                    B = B1*(11.9-1.9)/math.pi + 1.9
                    print("B", B)
 #                   tr.change(B)  

                    print("No.", j)
                    print("g= ", int(g*100)/100, "B0=  ", int((B0*10000)/10000*180/math.pi), "W", W)
                    print("m1", m1[0], m1[1], m1[2], int(w10*10)/10, int(w11*10)/10, int(w12*10)/10, int(W*10)/10)
                
                    with open("data2.csv", "a") as datafile:
#                        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
                        datafile.write(", %d"%j)
                        datafile.write(", %d"%W)
                        datafile.write(", %.01f"%g)
                        datafile.write(", %.02f"%B0)
                        datafile.write(", %d"%(B0*180/math.pi))
                        datafile.write(", %.01f"%x0)
                        datafile.write(", %.01f"%y0)
                        datafile.write(", %.01f\n"%d)
                        # datafile.write(" %d"%(j*20))
                        # datafile.write(", %d"%m1[0])
                        # datafile.write(", %d"%m1[1])
                        # datafile.write(", %d\n"%m1[2])
                    i = i +1
                     
                j = j + 1
            else:
                pass
            Wa = W
            
        except KeyboardInterrupt:

            GPIO.cleanup()            
