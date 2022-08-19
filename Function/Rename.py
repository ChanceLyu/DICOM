import os
import pydicom


# tag可能不存在，视具体DICOM文件而定

# 此函数只能根据PatientID更改DICOM文件名
# 若是需要通过其他tag命名，直接复制此函数并修改dicom_file.tag即可
# 如果出问题提醒/.DS_Store不存在，重新运行即可
# Windows系统需要修改/.DS_Store文件
def rename_dicom(file_path):
    # 遍历文件夹中所有DICOM文件
    for file in os.listdir(file_path):
        # 将文件夹中非DICOM文件删除,包括/.DS_Store
        # 建议备份以防文件夹中重要非DICOM文件被误删
        if os.path.exists(file_path + '/.DS_Store'):
            os.remove(file_path + '/.DS_Store')
        elif file[-4:] != '.dcm':
            os.remove(file_path + '/' + file)
        else:
            # 通过pydicom.dcmread读取DICOM文件
            # 萌新需要注意DICOM文件路径不能直接继承os.listdir路径
            dicom_file = pydicom.dcmread(file_path + '/' + file)
            # 读取PatientID
            tag = dicom_file.PatientID
            # 通过os.renames修改DICOM文件的名称
            # 需要注意前后名称均包含文件路径，并且勿忘文件扩展名
            old_name = file_path + '/' + file
            middle_name = file_path + '/hello.dcm'
            new_name = file_path + '/' + tag + '.dcm'
            # 中间名，待判断是否已经存在后再进行最终重命名
            os.renames(old_name, middle_name)
            # 通过while循环解决命名DICOM文件过程中已存在此名称的问题
            i = 0
            while os.path.exists(new_name):
                i += 1
                new_name = file_path + '/' + tag + '_' + str(i) + '.dcm'
            os.renames(middle_name, new_name)
        # 将可能再次生成的/.DS_Store删除
        if os.path.exists(file_path + '/.DS_Store'):
            os.remove(file_path + '/.DS_Store')
        else:
            continue

    print('Rename End!')


file_path = input('path')
rename_dicom(file_path)
