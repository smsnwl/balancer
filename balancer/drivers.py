import RPi.GPIO as GPIO
import time

class SN74595:
    def __init__(self, ser, rclk, srclk, oe=None, srclr=None):
        for pin in [ser, oe, rclk, srclk, srclr]:
            if pin is not None:
                GPIO.setup(pin, GPIO.OUT, initial = 0)
        self.ser = ser
        self.oe = oe
        self.rclk = rclk
        self.srclk = srclk
        self.srclr = srclr
        if srclr != None:
            GPIO.output(srclr, 1)
            
    def clear(self):
        GPIO.output(self.srclr, 0)
        GPIO.output(self.srclr, 1)

    def update(self):
        GPIO.output(self.rclk, 1)
        GPIO.output(self.rclk, 0)
        
    def streamin(self, statuslst):
        for s in statuslst:
            GPIO.output(self.ser, s)
            GPIO.output(self.srclk, 1)
            GPIO.output(self.srclk, 0)
            
    def negoe(self, status):
        GPIO.output(self.oe, status)

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

class Button():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)

    def waitforpress(self):
        GPIO.wait_for_edge(self.pin, GPIO.FALLING)
        
    def getinput(self):
        return GPIO.input(self.pin)

class InfraredPair():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def waitforpress(self):
        GPIO.wait_for_edge(self.pin, GPIO.FALLING)
        
    def getinput(self):
        return GPIO.input(self.pin)

    def getneginput(self):
        return (not GPIO.input(self.pin))

class Relay():
    def __init__(self, pin, init=0):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=init)

    def trigger(self,signal):
        GPIO.output(self.pin, signal)
        

class Stepper():
    def __init__(self, pen, pdr, ppl):
        self.pen = pen
        self.pdr = pdr
        self.ppl = ppl
        GPIO.setup([pen,pdr,ppl], GPIO.OUT, initial=0)

    def enable(self):
        GPIO.output(self.pen, 0)

    def disable(self):
        GPIO.output(self.pen, 1)

    def step(self, d):
        GPIO.output(self.pdr,d)
        GPIO.output(self.ppl,1)
        GPIO.output(self.ppl,0)
                
    def rotate(self, d, nstep, cond=lambda:True):
        self.enable()
        GPIO.output(self.pdr, d)
        i = 0;
        while i<nstep and cond():
            tau = 0.002
            GPIO.output(self.ppl,1)
            time.sleep(tau/2)
            GPIO.output(self.ppl,0)
            time.sleep(tau/2)
            i = i + 1
        return i

    def execute(self, d, l):
        GPIO.output(self.pdr, d)
        for i in range(len(l)):
            GPIO.output(self.ppl, 1)
            GPIO.output(self.ppl, 0)
            time.sleep(l[i])

    def execute(self, d, l, cond):
        GPIO.output(self.pdr, d)
        i = 0
        while i < len(l) and cond():
            GPIO.output(self.ppl, 1)
            GPIO.output(self.ppl, 0)
            time.sleep(l[i])
            i = i + 1
        return i
            
# Simple DC motor with two relays
class SDCM():
    def __init__(self, pina, pinb):
        GPIO.setup([pina, pinb], GPIO.OUT, initial=0)
        self.ma = Relay(pina)
        self.mb = Relay(pinb)
        
    def rotate(self, direction):
        self.ma.trigger(not(direction))
        self.mb.trigger(direction)

    def stop(self):
        self.ma.trigger(0)
        self.mb.trigger(0)
    
# L298 motor driver
class L298():
    def __init__(self, ppwma, ppwmb, f):
        GPIO.setup([ppwma,ppwmb], GPIO.OUT, initial=0)
        self.pwma = GPIO.PWM(ppwma, f)
        self.pwmb = GPIO.PWM(ppwmb, f)
        
    def start(self, cyclea, cycleb):
        self.pwma.start(cyclea)
        self.pwmb.start(cycleb)
        
    def change(self, cyclea, cycleb):
        self.pwma.ChangeDutyCycle(cyclea)
        self.pwmb.ChangeDutyCycle(cycleb)

    def stop(self):
        self.pwma.stop()
        self.pwmb.stop()

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
