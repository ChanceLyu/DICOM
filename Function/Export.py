import os
import pydicom
import openpyxl


# 此函数只能按特定序列顺序导出特定tag
# 若是需要按其他顺序导出tag，直接复制此函数并修改dicom_file.tag即可
# Windows系统需要修改/.DS_Store文件
def export_dicom(path_dicom, path_excel, s):
    # 使用openpyxl读取Excel文件和文件中的工作簿
    # s为工作簿序列数
    dicom_workbook = openpyxl.load_workbook(path_excel)
    # 注意工作簿序列数，以免误删
    dicom_sheet = dicom_workbook.worksheets[s]

    i = 2
    # 遍历文件夹中所有的DICOM文件
    for file in os.listdir(path_dicom):
        # 将文件夹中非DICOM文件删除,包括/.DS_Store
        # 建议备份以防文件夹中重要非DICOM文件被误删
        if os.path.exists(path_dicom + '/.DS_Store'):
            os.remove(path_dicom + '/.DS_Store')
        elif file[-4:] != '.dcm':
            os.remove(path_dicom + '/' + file)
        else:
            dicom_file = pydicom.dcmread(path_dicom + '/' + file)
            dicom_sheet['A' + str(i)].value = file[:-4]
            dicom_sheet['F' + str(i)].value = dicom_file.PatientSex
            dicom_sheet['G' + str(i)].value = dicom_file.PatientAge[1:-1]
            dicom_sheet['H' + str(i)].value = dicom_file.StudyDate[:4] + '/' + dicom_file.StudyDate[4:6] + '/' + \
                                              dicom_file.StudyDate[-2:]
            dicom_sheet['I' + str(i)].value = dicom_file.Modality
            dicom_sheet['J' + str(i)].value = dicom_file.PatientBirthDate[:4] + '/' + \
                                              dicom_file.PatientBirthDate[4:6] + '/' + dicom_file.PatientBirthDate[-2:]
            dicom_sheet['K' + str(i)].value = dicom_file.StationName
            dicom_sheet['L' + str(i)].value = dicom_file.StudyDescription
            dicom_sheet['M' + str(i)].value = dicom_file.Manufacturer
            dicom_sheet['N' + str(i)].value = dicom_file.ManufacturerModelName
            dicom_sheet['O' + str(i)].value = dicom_file.ViewPosition

        i += 1
        # 将可能再次生成的/.DS_Store删除
        if os.path.exists(path_dicom + '/.DS_Store'):
            os.remove(path_dicom + '/.DS_Store')
        else:
            continue

    dicom_workbook.save(path_excel)
    print('Export End!')