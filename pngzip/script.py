# coding:utf-8

import os
import os.path
rootdir = "./oldpng/"
newidr = "./newpng/"

new_create_name = "one"
jpegquality = 70


def getoldpng():
    items = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "DS_Store" in filename:
                continue
            if "png" in filename:
                items.append(parent + filename)
    return items


def getoldjpeg():
    items = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "DS_Store" in filename:
                continue
            if "png" not in filename:
                items.append(parent + filename)
    return items


def getnewpng():
    for parent, dirnames, filenames in os.walk(rootdir):
        items = []
        for filename in filenames:
            if "DS_Store" in filename:
                continue
            if new_create_name in filename:
                items.append(parent + filename)
        return items


def movePngToNew():
    newitems = getnewpng()
    os.system("mkdir newpng")
    for item in newitems:
        newitem = item.replace("oldpng", 'newpng').replace(new_create_name, "")
        cmd = "mv %s %s " % (item, newitem)
        os.system(cmd)


def zipJpeg(items):
    for item in items:
        print item
        cmd = "./jpegoptim -d " + newidr + \
            " -v -m{0} {1}".format(jpegquality, item)
        print cmd
        # cmd = "ls"
        one = os.popen(cmd)
        print "test"
        if "0.00" in one.read():
            newitem = item.replace("oldpng", "newpng")
            os.system("mv %s %s" % (item, newitem)
        print "end"


def zippng(items):
    for item in items:
        # tar = item.replace(item)
        cmd="./pngquant --quality=80-90 %s --ext %s" % (
            item, new_create_name + ".png")
        print cmd
        os.system(cmd)

zippng(getoldpng())
movePngToNew()
zipJpeg(getoldjpeg())
