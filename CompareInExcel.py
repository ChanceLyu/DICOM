import os
import openpyxl


path_file = input('file')
file_list = os.listdir(path_file)

if os.path.exists(path_file + '/.DS_Store'):
    file_list.remove('.DS_Store')

print(file_list)

path_excel = input('excel')
excel = openpyxl.load_workbook(path_excel)
sheet = excel.worksheets[0]

i = 2

for file in file_list:
    sheet['A' + str(i)].value = file[:-4]
    print(file[:-4])

    i += 1

print(i)
excel.save(path_excel)
