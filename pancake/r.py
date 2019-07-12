
import drivers
import math
import time
import sys
import RPi.GPIO as GPIO

global l0,l1,l2,l3,l4,p0,B0,p1,B1,b0,b1,ms

tt = 0  
# dir_steper:0or1:  0:down/1:up
dir = 1
ns = 600
ms = -50
msx = -500

p0 = 350
b0 = 0.1
p1 = 350
b1 = 0

l0 = 280
l1=l2=l3=l4=230

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
    # def rotate(self, d, nstep, cond=lambda:True):
        self.enable()
        GPIO.output(self.pdr, d)
        i = 0;
        while i<nstep and cond():
#            tau = 0.002   #guoce
            tau = 0.002   #nwl
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

class DualStepper:
    def __init__(self, ena0, dir0, pul0, ena1, dir1, pul1):
        GPIO.setup([ena0, dir0, pul0, ena1, dir1, pul1], GPIO.OUT, initial = 0)
        self.ena0 = ena0
        self.dir0 = dir0
        self.pul0 = pul0
        self.ena1 = ena1
        self.dir1 = dir1
        self.pul1 = pul1

    def rotate(self, nstep0, nstep1, display=True):
        # tau = 0.002
        tau = 0.008
        # Divide the time
        if nstep0 > 0:
            sgn0 = 1
        else:
            sgn0 = 0

        if nstep1 > 0:
            sgn1 = 1
        else:
            sgn1 = 0

        GPIO.output(self.dir0, sgn0)
        GPIO.output(self.dir1, sgn1)
        countdown0 = abs(nstep0)
        countdown1 = abs(nstep1)
        slotsize = max(min(countdown0, countdown1),1)
        # slot0 = countdown0/slotsize
        # slot1 = countdown1/slotsize
        slot0 = math.floor(countdown0/slotsize)
        slot1 = math.floor(countdown1/slotsize)
        if display:
            print('Directions %d %d' % (sgn0, sgn1))
            print('Slots %d %d' % (slot0, slot1))
            print('Slotssize %d'  % (slotsize))
            print('Remaining steps %d %d' % (countdown0, countdown1))
        # Alternate between two motors
        while countdown0 > 0 and countdown1 > 0:
            for i in range(countdown0):
#                if display:
#                    print('0')
                countdown0 = countdown0 - 1
                GPIO.output(self.pul0,1)
                time.sleep(tau)
                GPIO.output(self.pul0,0)
                time.sleep(tau)

            for i in range(countdown1):
                # if display:
                #     print('1')
                countdown1 = countdown1 - 1
                GPIO.output(self.pul1,1)
                time.sleep(tau)
                GPIO.output(self.pul1,0)
                time.sleep(tau)

##         Remaining steps for motor 0
        while countdown0 > 0:
            # if display:
            #     print('0')
            countdown0 = countdown0 - 1
            GPIO.output(self.pul0,1)
            time.sleep(tau)
            GPIO.output(self.pul0,0)
            time.sleep(tau)

        # Remaining steps for motor 0
        while countdown1 > 0:
            # if display:
            #     print('1')
            countdown1 = countdown1 - 1
            GPIO.output(self.pul0,1)
            time.sleep(tau)
            GPIO.output(self.pul0,0)
            time.sleep(tau)

def a1(p0,B0):
    global l0,l1,l2,l3,l4
    # 计算A点：

    g = (l1*l1-l0*l0/4+p0*p0-l2*l2)/(2*p0*math.cos(B0));
    k = (l0+2*p0*math.sin(B0))/(2*p0*math.cos(B0));
    a = k*k+1;
    b = l0-2*g*k;
    c = g*g+l0*l0/4-l1*l1;
    d = b*b-4*a*c
    ya = (-b-math.sqrt(b*b-4*a*c))/2/a;
    xa = math.sqrt(l1*l1-(ya+l0/2)*(ya+l0/2));

    yb = p0 * math.sin(B0)
    xb = p0 * math.cos(B0)

    l22 = round(math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)))
    if  l22 == l2:
        pass
    else:
        xa = -math.sqrt(l1*l1-(ya+l0/2)*(ya+l0/2));
    if B0 >= 0:
        a1 = math.atan((ya+l0/2)/xa);
        if xb == xa:
            a2 = math.pi/2
        elif xb > xa:
            a2 = math.atan((p0*math.sin(B0)+l0/2-l1*math.sin(a1))/(p0*math.cos(B0)-l1*math.cos(a1)));
        else:
            a2 = math.pi + math.atan((p0*math.sin(B0)+l0/2-l1*math.sin(a1))/(p0*math.cos(B0)-l1*math.cos(a1)));
    else:
        if xa == 0:
            a1 = -math.pi/2
        elif xa > 0:
            a1 = math.atan((ya+l0/2)/xa);
        else:
            a1 = -math.pi + math.atan((ya+l0/2)/xa);
        if xb == xa:
            a2 = -math.pi/2
        elif xb > xa:
            a2 = math.atan((p0*math.sin(B0)+l0/2-l1*math.sin(a1))/(p0*math.cos(B0)-l1*math.cos(a1)));
        else:
            a2 = math.pi - math.atan((p0*math.sin(B0)+l0/2-l1*math.sin(a1))/(p0*math.cos(B0)-l1*math.cos(a1)));

    # print("a1",int(a1*180/math.pi),"a2",int(a2*180/math.pi))
    return a1                   

def a4(p0,B0):                  
    global l0,l1,l2,l3,l4,a1
    # 计算C点：
    g1 = (l4*l4-l0*l0/4+p0*p0-l3*l3)/(2*p0*math.cos(B0))
    k1 = (l0-2*p0*math.sin(B0))/(2*p0*math.cos(B0))
    aa = 1+k1*k1
    b1 = 2*k1*g1-l0
    c1 = g1*g1+l0*l0/4-l4*l4

    yc = (-b1+math.sqrt(b1*b1-4*aa*c1))/2/aa
    xc = math.sqrt(l4*l4-(yc-l0/2)*(yc-l0/2))
    yb = p0 * math.sin(B0)
    xb = p0 * math.cos(B0)

    l33 = round(math.sqrt((xc-xb)*(xc-xb)+(yc-yb)*(yc-yb)))
    if l33 == l3:
        pass
    else:
        xc = -xc
    
    if B0 >= 0:
        if xc == 0:
            a4 = math.pi/2
        elif xc > 0:
            a4 = math.atan((yc-l0/2)/xc)
        else:
            a4 = math.pi + math.atan((yc-l0/2)/xc)
        if xc == xb:
            a3 = math.pi/2
        elif xc < xb:
            a3 = -math.atan((l4*math.sin(a4)+l0/2-p0*math.sin(B0))/(p0*math.cos(B0)-l4*math.cos(a4)));
        else:
            a3 = math.pi + math.atan((l4*math.sin(a4)+l0/2-p0*math.sin(B0))/(p0*math.cos(B0)-l4*math.cos(a4)));
    else:
        if xc == 0:
            a4 = -math.pi/2
        else:
            a4 = math.atan((yc-l0/2)/xc)
            # a4 = math.pi+math.atan((yc-l0/2)/xc)
        if xc == xb:
            a3 = -math.pi/2
        elif xc < xb:
            a3 = -math.atan((l4*math.sin(a4)+l0/2-p0*math.sin(B0))/(p0*math.cos(B0)-l4*math.cos(a4)));
        else:
            a3 = -math.pi - math.atan((l4*math.sin(a4)+l0/2-p0*math.sin(B0))/(p0*math.cos(B0)-l4*math.cos(a4)));
    
    # print("a3",int(a3*180/math.pi),"a4:",int(a4*180/math.pi))
    return a4

            
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



    
class Relay():
    def __init__(self, pin, init=0):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=init)
        
        def trigger(self,signal):
            GPIO.output(self.pin, signal)
            
class Button():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)
        
    def waitforpress(self):
        GPIO.wait_for_edge(self.pin, GPIO.FALLING)
        
    def getinput(self):
        return GPIO.input(self.pin)
            
class L298():
    def __init__(self,IN1 , IN2, IN3, IN4, f):
        GPIO.setup([IN1,IN2,IN3,IN4], GPIO.OUT, initial=0)
        self.IN1 = GPIO.PWM(IN1, f)
        self.IN2 = GPIO.PWM(IN2, f)
        self.IN3 = GPIO.PWM(IN3, f)
        self.IN4 = GPIO.PWM(IN4, f)

    def start(self, cyclea, cycleb, cyclec, cycled):
        self.IN1.start(cyclea)
        self.IN2.start(cycleb)
        self.IN3.start(cyclec)
        self.IN4.start(cycled)
        
def up_down(dir, ns):
#    ks = sj.rotate(dir, ns)
    ks = sj.rotate(dir, 60, btnZ.getinput)
    print("dir",dir, "up_down",ks)
    return

def wubi(p0,b0,p1,b1):    
    p0 = p0
    B0 = math.atan(b0)
    a10 = a1(p0,B0,)
    a40 = a4(p0,B0)
    print("p0=",p0,"B0=",(B0*180/math.pi))
    print("a10=",(a10*180/math.pi),"a40=",(a40*180/math.pi))

    print("P1,B1")
    p0 = p1
    B0 = math.atan(b1)

    a11 = a1(p0,B0)
    a41 = a4(p0,B0)
    # a41 = math.pi-a4(p0,B0)

    print("p1=",p0,"B1=",(B0*180/math.pi))
    print("a11=",(a11*180/math.pi),"a41=",(a41*180/math.pi))

    da1 = (a11 -a10)*180/math.pi
    da4 = (a41- a40)*180/math.pi
    print("da1:",round(da1*100)/100,"da4:",round(da4*100)/100)
    

    step_da1 = round(32*200*da1/360)
    step_da4 = round(32*200*da4/360)
    # step_da1 = round(200*da1/360)
    # step_da4 = round(200*da4/360)
    print("step_da1",step_da1,"step_da4",step_da4)
    ds.rotate(step_da1, step_da4)
    time.sleep(1)
    return

def bdxz(ms,msx):

    bd_xz.rotate(ms,msx)
    time.sleep(1)

    return

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    ds = DualStepper(26,19,13,6,5,0)
    bd_xz = DualStepper(22,27,17,18,15,14)
    sj = Stepper(11,9,10)

    # Buttons
    btnZ = Button(21)
    btnbd = Button(20)
    btnxz = Button(16)
        
    print("t0",time.time())
    ks = sj.rotate(dir, 600, btnZ.getinput)

    # up_down(dir, ns)
    # time.sleep(2)
    # up_down(1-dir, ns)
    # print("step1")
    # bd_xz.rotate(-200,300)

    # bdxz(-200,200)
    # bdxz(-ms,msx)
    # time.sleep(1)
    # bdxz(-ms,-msx)

    ## time.sleep(1)
    ## bdxz(0,msx)
    ## time.sleep(1)
    ## wubi(350,0,350,0.2)
    print("step3")
    # time.sleep(4)
#    wubi(350,0.2,350,0)
    print("step4")
    # up_down(1, ns)
    # print("step5")
    # print("step6")
    # xz_ni(txz_ni)
    # xz_shun(txz_shun)
    # print("step7")
    # up_down(0, ns)
    # print("step8")
    # fz_and_bd(tfz_and_bd)
    # print("step9")
    # bd_shun(tbd_shun)
    # print("step10")

    GPIO.cleanup()
