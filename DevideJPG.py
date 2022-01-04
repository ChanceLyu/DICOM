from PIL import Image
import os


JPG_file = input('The path of the JPG files: ')  # 图像文件目录
JPG_list = os.listdir(JPG_file)
if os.path.exists(JPG_file + '/.DS_Store'):
    JPG_list.remove('.DS_Store')  # 删除文件管理文件

for i in JPG_list:  # 截取左半边
    JPG = open(os.path.join(JPG_file, i), 'rb')
    img = Image.open(JPG)
    width = img.width
    height = img.height

    box = (0, 0, width * 0.5, height)
    img = img.crop(box)
    img.save(JPG_file + '/' + i.strip('.png') + '_L.png')
    # 根据生成文件扩展名和目录进行修改

for i in JPG_list:  # 截取右半边
    JPG = open(os.path.join(JPG_file, i), 'rb')
    img = Image.open(JPG)
    width = img.width
    height = img.height

    box = (width * 0.5, 0, width, height)
    img = img.crop(box)
    img.save(JPG_file + '/' + i.strip('.png') + '_L.png')
    # 根据生成文件扩展名和目录进行修改
