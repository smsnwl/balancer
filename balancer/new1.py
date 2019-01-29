
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
    for i in range(1):
        time.sleep(t)
        tr.start(3)
        print("tr", 10)
        tr.change(5)
        time.sleep(t)
        i = i+1
    
    h0 = SerialMeter(14, [15])
    h1 = SerialMeter(12, [1])
    h2 = SerialMeter(25, [18])
    print("请等待5秒")
    time.sleep(2)
    m00 = h0.getdv()
    m01 = h1.getdv()
    m02 = h2.getdv()
    print("请放置896.4g标准盘。（10秒内）")
    time.sleep(5)
    m10 = h0.getdv()
    m11 = h1.getdv()
    m12 = h2.getdv()
    print("getk()", m00, m01, m02, m10, m11, m12)
    
    k0 = (m10[0] - m00[0]) / (896.4/3)
    k1 = (m11[0] - m01[0]) / (896.4/3)
    k2 = (m12[0] - m02[0]) / (896.4/3)
    
    print("k0/k1/k2", int(k0), int(k1), int(k2))
    print("请在10s内取走标准盘!  (10秒内)")
    time.sleep(5)
    print("可以测试样品了")
    
    while True:
        try:
            time.sleep(1)
            m0 = h0.getdv()
            m1 = h1.getdv()
            m2 = h2.getdv()
#            print("m0/m1/m2", m0, m1, m2)
            w0 = m0[0] - m00[0]
            w1 = (m1[0] - m01[0])
            w2 = (m2[0] - m02[0])
            W = w0/k0 + w1/k1 + w2/k2
#            print("w0,w1,w2,W", w0,w1,w2,W)
            if W > 5 and  W - Wa > 5:
                time.sleep(1)
                for i in range(10000):
#                    tr.start(3)
                    time.sleep(0.01)
                    m0 = h0.getdv()
                    m1 = h1.getdv()
                    m2 = h2.getdv()
 #                   print("m0/m1/m2", m0, m1, m2)
                    w0 = m0[0] - m00[0]
                    w1 = m1[0] - m01[0]
                    w2 = m2[0] - m02[0]
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
                        B0 = 2*math.pi+math.atan(y0/x0)
                        B1 = math.pi+math.atan(y0/x0)
                    elif x0 < 0 and y0 >=0:
                        B0 = math.pi + math.atan(y0/x0)
                        B1 = B0 
                    elif x0 <0 and y0 < 0:
                        B0 = math.pi + math.atan(y0/x0)
                        B1 = math.atan(y0/x0)
                    else:
                        pass
                    B = B1*(11.9-1.9)/math.pi + 1.9
                    print("B", int(B*100)/100)
                    tr.change(B)  

                    print("No. j", j, "i", i)
                    print("g= ", int(g*100)/100, "B0=  ", int(B0*180/math.pi),"B1=  ", int(B1*180/math.pi))
                    print("m1", m0[0], m1[0], m2[0], int(w0/k0*10)/10, int(w1/k1*10)/10, int(w2/k2*10)/10, int(W*10)/10)
                
                    with open("datan.csv", "a") as datafile:
#                        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
                        # datafile.write(" %d"%j)
                        # datafile.write(", %d"%W)
                        # datafile.write(", %.01f"%g)
                        # datafile.write(", %.02f"%B0)
                        # datafile.write(", %d"%(B0*180/math.pi))
                        # datafile.write(", %.01f"%x0)
                        # datafile.write(", %.01f"%y0)
                        # datafile.write(", %.01f\n"%d)
#                        datafile.write(" %d"%(j*20))
                        datafile.write(" %d"%i)
                        datafile.write(", %d"%j)
                        datafile.write(", %d"%m0[0])
                        datafile.write(", %d"%m1[0])
                        datafile.write(", %d"%m2[0])
                        datafile.write(", %d"%w0)
                        datafile.write(", %d"%w1)
                        datafile.write(", %d"%w2)
                        datafile.write(", %d\n"%W)
                    i = i +1
                     
                j = j + 1
            else:
                pass
            Wa = W
            
        except KeyboardInterrupt:

            GPIO.cleanup()            
