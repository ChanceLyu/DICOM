from PIL import Image
import os

#  按照指定像素裁剪图片
JPG_file = input('The path of the JPG files: ')  # 图像文件目录
JPG_list = os.listdir(JPG_file)
if os.path.exists(JPG_file + '/.DS_Store'):
    JPG_list.remove('.DS_Store')  # 删除文件管理文件

for i in JPG_list:
    JPG = open(os.path.join(JPG_file, i), 'rb')
    img = Image.open(JPG)
    width = img.width
    height = img.height

    box = (width * 0.5 - 1493, height * 0.5 - 1528, width * 0.5 + 1493, height * 0.5 + 1528)
    img = img.crop(box)
    img.save(os.path.join(JPG_file, i))
