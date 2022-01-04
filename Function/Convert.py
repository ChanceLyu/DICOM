import os
import shutil

import SimpleITK
import numpy as np
import cv2
from tqdm import tqdm


# 此函数旨在将一个文件夹内的所有DICOM文件转换为JPG文件，并集中生成在某一制定文件夹内
# 目标文件夹必须是空的，否则会格式化
def convert_DICOM(img, low_window, high_window, save_path):
    # 将重要数据储存到lungwin中
    lungwin = np.array([low_window * 1., high_window * 1.])
    # 归一化
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])
    # 将像素值扩展到[0,255]
    newimg = (newimg * 255).astype('uint8')
    stacked_img = np.stack((newimg,) * 3, axis=-1)
    cv2.imwrite(save_path, stacked_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':

    dicom_dir = input('dicom_file')

    path = input('jpg_file')

    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    dicom_list = os.listdir(dicom_dir)
    if os.path.exists(dicom_dir + '/.DS_Store'):
        dicom_list.remove('.DS_Store')

    for i in tqdm(dicom_list):
        # 读取dicom文件
        dcm_image_path = os.path.join(dicom_dir, i)
        # 分离文件名与扩展名
        name, _ = os.path.splitext(i)
        # 设定jpg文件路径
        # 可直接更改生成图像的扩展名
        jpg_path = os.path.join(path, name + '.jpg')
        # 读取dicom文件的相关信息

        ds_array = SimpleITK.ReadImage(dcm_image_path)

        # 获取array
        img_array = SimpleITK.GetArrayFromImage(ds_array)
        # 获取单张shape，类似（1，height，width）
        shape = img_array.shape
        # 获取array中的height和width
        img_array = np.reshape(img_array, (shape[1], shape[2]))

        high = np.max(img_array)
        low = np.min(img_array)

        convert_DICOM(img_array, low, high, jpg_path)

    print('Convert End!')