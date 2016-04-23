# coding:utf-8

from PIL import Image, ImageDraw, ImageFont


# 图片右上角数字
def add(imgName):
    img = Image.open(imgName)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Library/Fonts/Sathu.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text(((width - 200), 10), '10086', font=myfont, fill=fillcolor)
    img.save("result.jpg", 'jpeg')


# add("image.jpeg")

