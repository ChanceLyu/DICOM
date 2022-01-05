from PIL import Image
import os

#  对比图片的尺寸，并找到最合适的裁剪尺寸

JPG_file = input('The path of the JPG files: ')  # 图像文件目录
JPG_list = os.listdir(JPG_file)
if os.path.exists(JPG_file + '/.DS_Store'):
    JPG_list.remove('.DS_Store')  # 删除文件管理文件

x = 0
y = 0
for i in JPG_list:
    JPG = open(os.path.join(JPG_file, i), 'rb')
    img = Image.open(JPG)
    width = img.width
    height = img.height

    if width > x:
        x = width

    if height > y:
        y = height

print(x)
print(y)
