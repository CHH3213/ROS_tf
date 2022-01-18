# --*--coding: utf-8 --*--
# @Time: 2022/1/18 21:51
# @Author: chh
# @PROJECT_NAME: test.
# @File: eulerTransoform.py
import numpy as np
import matplotlib.pyplot as plt
import string
import tf.transformations as tft


def euler_transform(r, p, y, order='szyx'):
    quat = tft.quaternion_from_euler(r, p, y, "szyx")
    euler_new = tft.euler_from_quaternion(quat, order)
    return euler_new



def readTxt(dir):
    '''
    读取txt，以空格分开
    :param dir: txt路径名
    :return: 数据
    '''
    data = []
    with open(dir, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split()
            numbers = []
            for l in line:
                l = float(l)
                numbers.append(l)
            data.append(numbers)
    # print(data)
    return data


def read_data(dir):
    data = np.genfromtxt(dir, dtype=[float, float, float, float, float])  # 将文件中数据加载到data数组里
    return data


def plot_rpy(x, y, z):
    plt.figure()
    ax1 = plt.axes(projection='3d')
    ax1.scatter(x, y, z, c='red')

    plt.show()


if __name__ == "__main__":
    # euler_transform(0,0,0)
    dir = "in_add_new.txt"
    data = readTxt(dir)
    data = np.array(data)
    # print(np.shape(data))
    euler_data = data[:, 0:3]
    print(np.shape(euler_data))
    print(np.min(euler_data[:, 2])* 180 / np.pi)
    print(np.max(euler_data[:, 2])* 180 / np.pi)
    eulers_new = []
    for r, p, y in zip(euler_data[:, 0], euler_data[:, 1], euler_data[:, 2]):
        # print(r,p,y)
        # print(type(r))
        euler = euler_transform(r, p, y, order="szyx")
        eulers_new.append(euler)
    eulers_new = np.array(eulers_new)
    # print(np.shape(eulers_new[:,2]))
    min = np.min(eulers_new[:,2])
    max = np.max(eulers_new[:,2])
    print(min * 180 / np.pi)
    print(max * 180 / np.pi)
    # print(np.shape(euler_data[:,0]),np.shape(euler_data[:,1]),np.shape(euler_data[:,2]))
    plot_rpy(euler_data[:, 0], euler_data[:, 1], euler_data[:, 2])
