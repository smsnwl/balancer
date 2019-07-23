import math
import RPi.GPIO as GPIO
import threading
import time
import csv

# pen0=4; pdr0=17;pul0=27;pen1=18;pdr1=23;pul1=24
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup([pen0,pdr0,pul0,pen1,pdr1,pul1],GPIO.OUT,initial=0)

class Double_stepper:
    def __init__(self, pen0, pdr0, pul0, pen1, pdr1, pul1):
        GPIO.setup([pen0, pdr0, pul0, pen1, pdr1, pul1], GPIO.OUT, initial = 0)
        self.pen0 = pen0
        self.pdr0 = pdr0
        self.pul0 = pul0
        self.pen1 = pen1
        self.pdr1 = pdr1
        self.pul1 = pul1

    def Step_a(self, nsa,t):
        GPIO.setmode(GPIO.BCM)
        # GPIO.output([pen0],GPIO.LOW)
        if nsa == 0:
            count0 += 0
            dia = 0
        elif nsa < 0:
            dia = 0
            # GPIO.output(pdr0,GPIO.LOW)
        else:
            dia = 1
            # GPIO.output(pdr0,GPIO.HIGH)
            count0=0
        for v in range(0,abs(nsa)):
            GPIO.output(self.pul0,1)
            time.sleep(t/nsa)
            GPIO.output(self.pul0,0)
        count0 += 1
        with open("data1.csv", "a") as datafile:
            datafile.write("  %d"%count0)
        return dia,count0
    def Step_b(self,nsb,t):
        GPIO.setmode(GPIO.BCM)
        # GPIO.output([pen1],GPIO.LOW)
        if nsb == 0:
            count1+=0
            dib = 0
        elif nsb < 0:
            dib = 0
            # GPIO.output(pdr1,GPIO.LOW)
        else :
            dib = 1
            # GPIO.output(pdr1,GPIO.HIGH)
            count1=0
        for i in range(0,abs(nsb)):
            GPIO.output(self.pul1,1)
            time.sleep(t/nsb)
            GPIO.output(self.pul1,0)
            count1+=1
        with open("data1.csv", "a") as datafile:
            datafile.write(",  %d"%count1)

    def double_step(self, nsa, nsb, t):
        self.nsa = nsa
        self.nsb = nsb
        self.t = t
        threads=[]
        threads.append(threading.Thread(target=self.Step_a(nsa,t)))
        threads.append(threading.Thread(target=self.Step_b(nsb,t)))
        for t in threads:
            t.start()
        with open("data1.csv", "a") as datafile:
            datafile.write("  %d"%nsa)
            datafile.write("  %d\n"%nsb)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    # nsa=13
    # nsb=170
    # t=5

    ds1 = Double_stepper(4,17,27,18,23,24)
    # ds2 = Double_stepper(4,17,27,18,23,24)

    ds1.double_step(13,170,5)

    GPIO.cleanup()
