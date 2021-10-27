import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pydicom
from tqdm import tqdm
import SimpleITK


def is_dicom_file(filename):
    file_stream = open(filename, 'rb')
    file_stream.seek(128)
    data = file_stream.read(4)
    file_stream.close()
    if data == b'DICM':
        return True
    return False


def load_patient(src_dir):
    files = os.listdir(src_dir)
    slices = []
    for s in files:
        if is_dicom_file(src_dir + '/' + s):
            instance = pydicom.read_file(src_dir + '/' + s)
            slices.append(instance)

    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
    return slices


def get_pixels_hu_by_simpleitk(dicom_dir):
    reader = SimpleITK.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    img_array = SimpleITK.GetArrayFromImage(image)
    img_array[img_array == -2000] = 0
    return img_array




# dicom文件目录
dicom_dir = '/Users/lvqianyu/Downloads/分类数据存档/膝 型号分类/尚方宝剑'
# 读取dicom文件的元数据(dicom tags)
# slices = load_patient(dicom_dir)
# print('The number of dicom files : ', len(slices))
# 提取dicom文件中的像素值
image = get_pixels_hu_by_simpleitk(dicom_dir)
for i in tqdm(range(image.shape[0])):
    # 输出png文件目录
    img_path = "/Users/lvqianyu/Downloads/分类数据存档" + str(i).rjust(4, '0') + "_i.png"
    org_img = image[i] * 20
    # 保存图像数组
    cv2.imwrite(img_path, org_img)

# /Users/lvqianyu/Downloads/分类数据存档/膝 型号分类/尚方宝剑
# /Users/lvqianyu/Downloads/分类数据存档/膝 型号分类/水滴/DR1209532.dcm
