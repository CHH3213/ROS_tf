# --*--coding: utf-8 --*--
# @Time: 2022/1/18 21:51
# @Author: chh3213
# @PROJECT_NAME: test.
# @File: eulerTransoform.py
"""
欧拉角不同顺序的转换
"""
import numpy as np
import matplotlib.pyplot as plt
import string
import tf.transformations as tft
from rotate_calculation import Rotate

def euler_transform(r, p, y, order='szyx'):
    """
    欧拉角不同顺序转换
    :param r:
    :param p:
    :param y:
    :param order: 转换顺序
    :return:
    """
    quat = tft.quaternion_from_euler(r, p, y, "szyx")
    euler_new = tft.euler_from_quaternion(quat, order)
    return euler_new


def readTxt(dir):
    '''
    file方式读取txt，以空格分开
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
    """
    画三维图
    :param x:
    :param y:
    :param z:
    :return:
    """
    plt.figure()
    ax1 = plt.axes(projection='3d')
    ax1.scatter(x, y, z, c='red')

    plt.show()


def change_axis(r, p, y, rot_r,rot_p,rot_y):
    """
    旋转当前的姿态,均为弧度制
    :param r: 当前姿态的roll
    :param p: 当前姿态的pitch
    :param y: 当前姿态的yaw
    :param rot_r: 绕x轴旋转roll_r
    :param rot_p: 绕y轴旋转roll_p
    :param rot_y: 绕z轴旋转roll_y
    :return:
    """
    quat_axis = tft.quaternion_from_euler( rot_r,rot_p,rot_y, 'szyx')
    # print(quat_axis)
    # quat_axis = np.array([0, 0, rot_ang_zaxis, 0])
    ro = Rotate()
    quat = tft.quaternion_from_euler(r, p, y, "szyx")
    # rotated_quat = ro.rotated_vector(quat_axis,quat)
    rotated_quat = tft.quaternion_multiply(quat_axis, tft.quaternion_multiply(quat, tft.quaternion_inverse(quat_axis)))
    euler_new = tft.euler_from_quaternion(rotated_quat, 'szyx')
    # print(ro.eulerAnglesToRotationMatrix(rot_r,rot_p,rot_y))
    # euler_new = np.einsum("ij,j->i",ro.eulerAnglesToRotationMatrix([rot_r, rot_p, rot_y]),np.array([r,p,y]))
    # matrix = np.dot(ro.eulerAnglesToRotationMatrix([rot_r, rot_p, rot_y]), ro.eulerAnglesToRotationMatrix([r, p, y]))
    # euler_new = tft.euler_from_matrix(matrix,axes="szyx")
    # print(np.shape(euler_new))
    return euler_new

def save_txt(dir,data):
    """
    numpy的方式保存txt
    :param dir: 保存路径
    :param data: 保存数据
    :return:
    """
    np.savetxt(dir, data)

def read_txt(dir):
    """
    numpy的方式加载txt
    :param dir:
    :return:
    """
    data = np.loadtxt(dir)
    return data

def rot_test( rot_r=0.1,rot_p=-0.0,rot_y=-0.):
    """

    :param rot_r: 旋转的roll
    :param rot_p: 旋转的pitch
    :param rot_y: 旋转的yaw
    :return:
    旋转矩阵： rot_r=-0.1,rot_p=-0.1,rot_y=0
    四元数：rot_r=0.1,rot_p=-0.0,rot_y=-0.
    """
    dir = "in_add_new.txt"
    data = read_txt(dir)
    # print(data)
    data = np.array(data)
    data_nonzero = []
    for i, d in enumerate(data):
        # print(d)
        if np.all(d)!=0:
            # print("aa")
            data_nonzero.append(d)
    data = np.array(data_nonzero)
    # print(data)
    print(np.shape(data))
    euler_data = data[:, 0:3]
    min = np.min(euler_data[:, 2]) * 180 / np.pi
    max = np.max(euler_data[:, 2]) * 180 / np.pi
    min_roll = np.min(euler_data[:, 0]) * 180 / np.pi
    max_roll = np.max(euler_data[:, 0]) * 180 / np.pi
    min_pitch = np.min(euler_data[:, 1]) * 180 / np.pi
    max_pitch = np.max(euler_data[:, 1]) * 180 / np.pi
    print("============origin===============")
    print("roll", min_roll, max_roll)
    print("pitch", min_pitch, max_pitch)
    print("yaw", min, max)
    # count = 0
    # for yaw in euler_data[:, 2]:
    #     if yaw * 180 / np.pi < 2 and yaw * 180 / np.pi > -2:
    #         count += 1
    # print("count", count)
    print("------------------------------")
    print("=============new==============")
    eulers_new = []
    for r, p, y in zip(euler_data[:, 0], euler_data[:, 1], euler_data[:, 2]):
        euler = change_axis(r, p, y, rot_r,rot_p,rot_y)
        eulers_new.append(euler)
    eulers_new = np.array(eulers_new)
    min = np.min(eulers_new[:, 2]) * 180 / np.pi
    max = np.max(eulers_new[:, 2]) * 180 / np.pi
    min_roll = np.min(eulers_new[:, 0]) * 180 / np.pi
    max_roll = np.max(eulers_new[:, 0]) * 180 / np.pi
    min_pitch = np.min(eulers_new[:, 1]) * 180 / np.pi
    max_pitch = np.max(eulers_new[:, 1]) * 180 / np.pi
    print("roll", min_roll, max_roll)
    print("pitch", min_pitch, max_pitch)
    print("yaw", min, max)
    count = 0
    for yaw in eulers_new[:, 2]:
        if yaw * 180 / np.pi < 2 and yaw * 180 / np.pi > -2:
            count += 1
    print("count", count)
    # print(np.shape(euler_data[:,0]),np.shape(euler_data[:,1]),np.shape(euler_data[:,2]))
    plot_rpy(euler_data[:, 0], euler_data[:, 1], euler_data[:, 2])
    save_txt("nd.txt", eulers_new)
if __name__ == "__main__":
    # rot_test()
    # data = read_txt("afile.txt")

    # print(np.shape(data))
    data = read_txt("new_data_euler.txt")
    data_new = []

    print(np.shape(data))
    for angle in data:
        if(-20<angle[0]*180/np.pi<20 and -50<angle[1]*180/np.pi<-15 and -4<angle[2]*180/np.pi<4):
            # print(angle)
            data_new.append(angle)
    save_txt("new_data11.txt",data_new)
    print(np.shape(data_new))