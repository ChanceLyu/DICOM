from PIL import Image
import os

for a in ['/Users/lvqianyu/Downloads/JPG分类（1000*1000）/膝关节 阴性',
          '/Users/lvqianyu/Downloads/JPG分类（1000*1000）/膝关节 阳性',
          '/Users/lvqianyu/Downloads/JPG分类（1000*1000）/髋关节 阴性',
          '/Users/lvqianyu/Downloads/JPG分类（1000*1000）/髋关节 阳性']:
    JPG_file = a  # 图像文件目录
    JPG_list = os.listdir(JPG_file)
    if os.path.exists(JPG_file + '/.DS_Store'):
        JPG_list.remove('.DS_Store')  # 删除文件管理文件

    for i in JPG_list:  # 截取左半边
        JPG = open(os.path.join(JPG_file, i), 'rb')
        img = Image.open(JPG)
        width = img.width
        height = img.height

        box = (width * 0.5 - 500, height * 0.5 - 500, width * 0.5 + 500, height * 0.5 + 500)
        img = img.crop(box)

        img.save(JPG_file + '/' + i.strip('.jpg') + '.jpg')
