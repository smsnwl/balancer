from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


'''
w0:重物均值
w1:传感器1
w2:传感器2
w2:传感器3
'''


def pot_show(arr, til):
    """画正态分布叠加直方图"""

    mean = arr.mean()   # 均值
    std = arr.std()  # 方差

    x = np.arange(arr.min()-1, arr.max()+1, 0.5)  # 定图区间
    y = scipy.stats.norm.pdf(x, mean, std)  # 正态分布

    plt.plot(x, y, '#FF6347', linewidth=2)  # 画图
    plt.hist(arr, bins=20, color='b', alpha=0.5,
             rwidth=0.9, density=True)  # 叠加直方图

    plt.title(til)
    plt.xlabel('weight:g')
    plt.ylabel('Probability:%')
    plt.show()


def mean_fun(arr):
    return arr.mean(), arr.std()


if __name__ == "__main__":

    arr_data = read_csv('data999.csv')   # 取数
#    arr_data = read_csv('0318_1.csv')   # 取数

    # 作图
    # data_w0 = arr_data['w0']
    # pot_show(data_w0, 'w0')
    # num_0 = mean_fun(data_w0)
    # print('均值{:.2f},方差{:.2f}'.format(num_0[0], num_0[1]))

    # data_w1 = arr_data['w1']/10000
    # pot_show(data_w1, 'w1')
    # num_1 = mean_fun(data_w1)
    # print('均值{:.2f},方差{:.2f}'.format(num_1[0],num_1[1]))

    data_w2 = arr_data['w2']
    pot_show(data_w2, 'w2')
    num_2 = mean_fun(data_w2)
    print('均值{:.2f},方差{:.2f}'.format(num_2[0],num_2[1]))

    # data_w3 = arr_data['w3']
    # pot_show(data_w3, 'w3')
    # num_3 = mean_fun(data_w3)
    # print('均值{:.2f},方差{:.2f}'.format(num_3[0], num_3[1]))
