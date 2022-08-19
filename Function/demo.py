import os
import glob
import pydicom

import pandas as pd
import numpy as np

from collections import OrderedDict
import argparse


def main(input, output):
    if os.path.exists(input + '/.DS_Store'):
        os.remove(input + '/.DS_Store')

    data_root = input
    dirs = os.listdir(data_root)
    PatientID = []
    PatientName = []
    PatientSex = []
    PatientAge = []
    PatientWeight = []
    PatientStudyDescription = []
    items = {'PatientID': PatientID, 'PatientName': PatientName, 'PatientSex': PatientSex,
             'PatientAge': PatientAge, 'PatientWeight': PatientWeight}
    for folder in dirs:

        paths_ = os.path.join(data_root, folder)

        if os.path.exists(paths_ + '/.DS_Store'):
            os.remove(paths_ + '/.DS_Store')

        if os.path.exists(paths_ + '/StudyInfo.dat'):
            os.remove(paths_ + '/StudyInfo.dat')
        paths = os.listdir(paths_)


        PATH = os.path.join(paths_, paths[0])
        print(PATH)
        dcms = glob.glob(os.path.join(PATH, '*.[dD]cm'))
        print(dcms)

        dcm = dcms[0]

        img = pydicom.read_file(dcm)
        for item in items.keys():
            temp = items[item]
            try:
                value = img.__getattr__(item)

                temp.append(value)
            except Exception as e:
                print(e)
                temp.append(None)
            # PatientID.append(img.get_item("PatientID"))
            # PatientName.append(img.PatientName)
            # PatientSex.append(img.PatientSex)
            # PatientAge.append(img.PatientAge)
            # PatientWeight.append(img.PatientWeight)
        # except Exception as e:
        #     print(e)
        if hasattr(img, 'StudyDescription'):
            PatientStudyDescription.append(img.StudyDescription)
        else:
            PatientStudyDescription.append(' ')

    columns = OrderedDict({'ID': PatientID,
                           'Name': PatientName,
                           'Sex': PatientSex,
                           'Age': PatientAge,
                           'Weight': PatientWeight,
                           'StudyDescription': PatientStudyDescription})
    df = pd.DataFrame.from_dict(columns)
    df.to_excel(output)


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    # parse.add_argument('--input', type=str, default='H:\\MRI')
    # parse.add_argument('--output', type=str, default=r'H:\\MRI')
    parse.add_argument('--input', type=str, default=r'/Users/lvqianyu/Downloads/2021-03')
    parse.add_argument('--output', type=str, default=r'/Users/lvqianyu/Downloads/test3.xlsx')
    args = parse.parse_args()
    main(args.input, args.output)
