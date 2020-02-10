# -*- coding: utf-8 -*- 
"""
@project: MaskDetection_yolo3
@file: face_mask_annotation.py
@Author: xiaowenwen 
@time: 2020/2/10 20:15
@desc:
"""

import xml.etree.ElementTree as ET
from os import getcwd

sets = ['train',  'val', 'test']
classes = ["rightmask", "wrongmask", "nomask"]

dataPath = "dataset/face_mask/data/"
labelPath = "dataset/face_mask/label/"

def convert_annotation(image_id, list_file):
    in_file = open('dataset/face_mask/label/%s.xml' % image_id)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for image_set in sets:
    image_ids = open('dataset/face_mask/data_list/%s.txt' % image_set).read().strip().split()
    list_file = open('face_mask_%s.txt' % image_set, 'w')
    for image_id in image_ids:
        print(image_id)
        list_file.write('%s/dataset/face_mask/data/%s.jpg'%(wd, image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()
