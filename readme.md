## MaskDetection_yolo3

基于深度学习的口罩检测项目

### 背景

2020年初，新型冠状病毒形势比较严峻，针对公共场合检测人员是否佩戴口罩的需求，有网友做了口罩检测数据集，故拿来做个目标检测的练习。

### 环境

- **Python：** 3.6.5
- **Tensorflow：** 1.12.0
- **Keras:** 2.2.4
- **GTX 1050**

### 数据集

[口罩检测数据集](https://github.com/hikariming/virus-mask-dataset)

### 使用方法

#### 测试

    python yolo_video.py --image

#### 训练

##### 数据预处理

将口罩数据集下载至dataset中，并解压，然后执行

    python dataset/preprocess.py  ##数据清洗并划分训练集和测试集
    python face_mask_annotation.py  ## 生成数据集索引


##### 执行训练

    python train.py

### 训练参数

- **分辨率：** 224*224
- **批次大小：** 4
- **迭代次数：** 100

### 问题

- 数据集规模小，分类效果不好
- 蹲在家里只能用笔记本跑，分辨率和批次大小上不去，训练效果并不好

### 参考文献

1. 数据集：[口罩检测数据集](https://github.com/hikariming/virus-mask-dataset)
1. 基于keras的YOLO框架：[qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3)
1. MaskDetect：[ztjryg4/MaskDetect](https://github.com/ztjryg4/MaskDetect)



