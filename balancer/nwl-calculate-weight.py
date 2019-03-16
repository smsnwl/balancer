
import RPi.GPIO as GPIO
from hx711 import HX711
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

DT1, SCK1 = 17, 18
DT2, SCK2 = 22, 23
DT3, SCK3 = 26, 20

DIF = 250  # 波动系数

# 称重系数
ROT = [298.97833333333955, 295.845, 298.45, 302.64]

R = 183   # 圆盘半径

def zero_fun():
    """初始值"""
    yime.sleep(0.5)
    zero1 = HX711(SCK1, DT1).getdv()
    zero2 = HX711(SCK2, DT2).getdv()
    zero3 = HX711(SCK3, DT3).getdv()
    print("(zero1 + zero2 + zero3)/3, zero1, zero2, zero3",(zero1 + zero2 + zero3)/3, zero1, zero2, zero3)
    return (zero1 + zero2 + zero3)/3, zero1, zero2, zero3,


def calculate_ratio(W=896.4):
    """计算称重系数"""
    print('请在5秒内放{}g标准盘...'.format(W))
    time.sleep(5)
    cont = zero_fun()
    d = list(map(lambda x, y: x - y, cont, initial))
    r = [i/W for i in d]
    print("r",r)
    return r


def calculate_weight():
    """计算每个秤的重量"""
    cont = zero_fun()
    d = list(map(lambda x, y: x - y, cont, initial))    # 做差
    d = list(map(lambda x: x if x > DIF else 0, d))  # 过滤波动
    w = list(map(lambda x, y: x / y, d, ROT))   # 称重
    print("w######",w)
    return w

def weigth_to_csv(file,lst,lenth):
    """将列表写入文件"""
    with open(file, 'a') as csvfile:
        for i, v in enumerate(lst):
            csvfile.write(str(v)+',')
        csvfile.write(str(lenth)+'\n')
        
def coordinate(m,M,R):
    """
    y = -((2*R)/(3*M))x + 1.667R 线性关系式
    
    x：子秤重量
    y：距离子秤距离
    """
    return -((2*R)/(3*M))*m + 1.667*R

initial = zero_fun()

# 初始坐标
position = [0,0,0]

if __name__ == '__main__':

    r = calculate_ratio(896.4)  # 计算重量系数
    print("r",r)

    while True:
        print("请在3秒内放置砂轮")
        time.sleep(3)
        w = calculate_weight()    
        weigth_to_csv('0310.csv',w,6.28318530717959)  #导出数据
        
        if w[0] < 3:
            position = [0,0,0]
        else:
            position[0] = coordinate(w[1],w[0],R)
            position[1] = coordinate(w[2],w[0],R)
            position[2] = coordinate(w[3],w[0],R)
        print('实 重：{:.2f}g;\n秤--1：{:.2f}g;\n秤--2：{:.2f}g;\n秤--3：{:.2f}g;'.format(
            w[0], w[1], w[2], w[3]))
        print(position)
        print('*'*20)
