import RPi.GPIO as GPIO
import threading
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

a=[4,17,27,18]
b=[22,23,24,25]

for t in a,b:
    GPIO.setup(t,GPIO.OUT)

def step_a(nsa,dia,t,n0):
    arr_a=[0,1,2,3];
    if dia!=1:
        arr_a=[3,2,1,0];
    for i in range(0,n0):
        for x in arr_a:
            time.sleep((t/4)/nsa)
            for j in range(0,4):
                if j==x:
                    GPIO.output(a[j],True)
                else:
                    GPIO.output(a[j],False)
    
def step_b(nsb,dib,t,n1):
    arr_b=[0,1,2,3];
    if dib!=1:
        arr_b=[3,2,1,0];
    for i in range(0,n1):
        for v in arr_b:
            time.sleep((t/4)/nsb)
            for j in range(0,4):
                if j==v:
                    GPIO.output(b[j],True)
                else:
                    GPIO.output(b[j],False)

def double_step(nsa,dia,nsb,dib,t):
    count=0
    count1=0
    time0=time.time()
    if nsa>=nsb and nsa!=0 and nsb!=0:
        n0=round(nsa/nsb)
        n1=1
        print("nsa>nsb   n0",n0)
    if nsa<=nsb and nsa!=0 and nsb!=0:
        n0=1
        n1=round(nsb/nsa)
        print("nsa<nsb   n1",n1)
    if nsa==0 or nsb==0:
        n0=1
        n1=1
    while True:
        count+=n0
        count1+=n1
        if nsb==0:
            step_a(nsa,dia,t,n0)
            if count>=nsa:
                break
        if nsa==0:
            step_b(nsb,dib,t,n1)
            if count1>=nsb:
                break
        else:
            ksa = step_a(nsa,dia,t,n0)
            ksb = step_b(nsb,dib,t,n1)
            if count>=nsa or count1>=nsb:
                break

if __name__ == '__main__':
    nsa = 11
    dia = 1
    nsb = 1300
    dib = 1
    t = 5

    double_step(nsa,dia,nsb,dib,t)
    
    with open("data1.csv", "a") as datafile:
        datafile.write(time.strftime("%Y-%m-%d-%H-%M-%S"))
        datafile.write("  %d"%nsa)
        datafile.write("  %d"%dia)
        datafile.write("  %d"%nsb)
        datafile.write("  %d"%dib)
        datafile.write(", %d\n"%t)
