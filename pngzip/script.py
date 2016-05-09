# coding:utf-8

import os
import os.path
rootdir = "./oldpng/"
newidr = "./newpng/"

new_create_name = "one"


def getoldpng():
    for parent, dirnames, filenames in os.walk(rootdir):
        items = []
        for filename in filenames:
            if "DS_Store" in filename:
                continue
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
    for item in newitems:
        newitem = item.replace("oldpng", 'newpng').replace(new_create_name, "")
        cmd = "mv %s %s " % (item, newitem)
        os.system(cmd)


def zippng(items):
    for item in items:
        # tar = item.replace(item)

        cmd = "./pngquant --quality=80-90 %s --ext %s" % (
            item, new_create_name + ".png")
        print cmd
        os.system(cmd)
# png(getoldpng())
zippng(getoldpng())
movePngToNew()
