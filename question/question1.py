# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import requests
import StringIO
# 图片右上角数字


def add(imgName):
    img = Image.open(imgName)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('./heiti.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text(((width - 200), 10), '10086', font=myfont, fill=fillcolor)
    img.save("result.jpg", 'jpeg')

    new_image = Image.new('RGBA', (500, 500), (255, 255, 255))
    new_image.save("re.png", 'png')


def getImage(image_url):
    r = requests.get(image_url)
    im = Image.open(StringIO.StringIO(r.content))
    return im


def roll(image, delta): v
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    print delta
    if delta == 0:
        return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize - delta, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))

    return image


def rotate(im, rotateNum):
    img = Image.open("hyaline.png")
    im = im.resize((150, 150))
    img.paste(im, (10, 10))
    img = img.rotate(rotateNum)


def calculate():
    pass


def paste():
    img = Image.open("hyaline.png")
    url = "http://h5img.yyyad.com/h5img/08269a70103dd72b8ef0ef32c51c29bd852cc756.jpg"
    im = getImage(url)
    # print "im",im.getbbox()
    imbox = im.getbbox()
    # im = im.resize((150,150))
    im.show()
    img.paste(im, (10, 10))
    img.show()
    img = img.rotate(15)
    img.save("20.png")
    return img


def test():
    paste()
    back = (640, 441)
    new_image = Image.new('RGBA', back, (255, 255, 255))
    print "new_image", new_image.getbbox()
    print "new_image", new_image.mode
    print "new_image", new_image.split()
    # new_image.show()
    img = Image.open("mother.png")
    o_img = Image.open("mother1.png")
    print 'img', img.getbbox()
    print "img", img.mode
    print "img", img.split()
    r, g, b, a = img.split()
    im = paste()
    url = "http://h5img.yyyad.com/h5img/08269a70103dd72b8ef0ef32c51c29bd852cc756.jpg"
    # im = getImage(url)
    # print "im",im.getbbox()
    imbox = im.getbbox()
    x = 344
    y = 50
    new_box = (imbox[0] + x, imbox[1] + y, imbox[2] + x, imbox[3] + y)

    new_image.paste(im, new_box, im.split()[3])
    # new_image.show()
    new_image.paste(o_img, (0, 0), a)
    new_image.save("dd.png")


def finalend():
    back_size = (538, 747)
    back_im = Image.new('RGBA', back_size, (255, 255, 255))
    im = getImage(
        "http://7xltx1.com2.z0.glb.qiniucdn.com/1570081-3090c6fbaa0725aa.jpg?imageMogr2/crop/!200x200a200a50/rotate/-6/")
    im2 = getImage(
        "http://7xltx1.com2.z0.glb.qiniucdn.com/1570081-3090c6fbaa0725aa.jpg?imageMogr2/crop/!200x200a200a50/rotate/7/")
    # im.show()

    img = Image.open("./card.png")

    back_im.paste(im, (32, 200))
    print img.split()
    back_im.paste(im2, (270, 160))

    font = (260, 340)

    back_im.paste(img, (0, 0), img.split()[3])
    # back_im.save("img.png")
    draw = ImageDraw.Draw(back_im)
    myfont = ImageFont.truetype('./heiti.ttf', size=30)
    fillcolor = "#ffffff"
    # width, height = img.size
    draw.text(font, '80%', font=myfont, fill=fillcolor)
    y = 0
    new_font_size = (108, 450 + y)

    myfont = ImageFont.truetype('./heiti.ttf', size=17)
    # '/Library/Fonts/Tahoma.ttf', size=30)
    fillcolor = "#333333"
    draw.text(new_font_size, u'妈妈我爱你\n你好啊', font=myfont, fill=fillcolor)
    back_im.save("img.png")

    # print img.getbbox()

if __name__ == '__main__':
    finalend()
    # url = "http://www.83133.com/uploads/image/20160407/1459998602443489.jpg"
    # url = "http://7xltx1.com2.z0.glb.qiniucdn.com/1570081-3090c6fbaa0725aa.jpg?imageMogr2/crop/!200x200a200a50/rotate/-5/"
    # im = getImage(url)
    # im = im.rotate(10)
    # im.show()
    # add()
    # add("image.jpeg")

    # new_image.paste(img,img.getbbox(),a)
    # new_image.show()
    # img.save("dd.png")
    # im = roll(im,10)
    # im.show()
    # out = im.rotate(90)
    # out = im.transpose(Image.ROTATE_90)
    # out.show()

    # print a
    # pass

# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print BASE_DIR
# MEDIA_ROOT = os.path.sep.join([BASE_DIR, 'media'])
# print MEDIA_ROOT
# os.path.abspath
