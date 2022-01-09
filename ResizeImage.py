from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=600, height=600):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob("/Users/lvqianyu/Downloads/JPG分类（1300*1300）/Positive_Knee_DR1027019_1.jpg"):
    convertjpg(jpgfile, "/Users/lvqianyu/Downloads/JPG分类（1300*1300）")
