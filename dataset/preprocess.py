# -*- coding: utf-8 -*- 
"""
@project: MaskDetection_yolo3
@file: preprocess.py
@Author: xiaowenwen 
@time: 2020/2/10 19:26
@desc:
"""

import os
import shutil
import random

dataPath_old = "part1/data/"
labelPath_old = "part1/label/"
dataPath_new = "face_mask/data/"
labelPath_new = "face_mask/label/"

if not os.path.exists(dataPath_new):
    os.mkdir(dataPath_new)
if not os.path.exists(labelPath_new):
    os.mkdir(labelPath_new)

datalist = os.listdir(dataPath_old)

# 数据清洗
for data in datalist:
    (filename, extension) = os.path.splitext(data)
    if filename.find(" (1)") == -1 and os.path.exists(labelPath_old + filename + ".xml"):  # 去掉重复数据
        print(data)
        old_path_data = os.path.join(dataPath_old, data)
        new_path_data = os.path.join(dataPath_new, filename + ".jpg")  # 规范文件后缀名
        old_path_label = os.path.join(labelPath_old, filename + ".xml")
        new_path_label = os.path.join(labelPath_new, filename + ".xml")
        shutil.copyfile(old_path_data, new_path_data)
        shutil.copyfile(old_path_label, new_path_label)


# 构建数据集
val_percent = 0.2
test_num = 10
datalist = os.listdir(dataPath_new)
num = len(datalist)
numlist = range(num)
train = random.sample(numlist, num-test_num)
val = random.sample(train, int((num-test_num) * val_percent))

if not os.path.exists("face_mask/data_list/"):
    os.mkdir("face_mask/data_list/")

ftrain = open('face_mask/data_list/train.txt', 'w')
fval = open('face_mask/data_list/val.txt', 'w')
ftest = open('face_mask/data_list/test.txt', 'w')

for i in numlist:
    (filename, extension) = os.path.splitext(datalist[i])
    if i in train:
        if i in val:
            fval.write(filename+"\n")
        else:
            ftrain.write(filename+"\n")
    else:
        ftest.write(filename+"\n")

ftrain.close()
fval.close()
ftest.close()
