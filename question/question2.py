# coding:utf-8

# lll = "qwertyuiopasdfghjklzxcvbnm1234567890ZAQXSWCDEVFRBGTNHYMJUKILOP"
# print set(lll)
import random
mode = ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'A', 'C', 'B', 'E',
        'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S',
        'R', 'U', 'T', 'W', 'V', 'Y', 'X', 'Z', 'a', 'c', 'b', 'e', 'd', 'g',
        'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u',
        't', 'w', 'v', 'y', 'x', 'z']


def getRandom(num):
    apps = []
    while num:
        apps.append(random.choice(mode))
        num -= 1
# pass
    return ''.join(apps)
# print
if __name__ == '__main__':
    for i in range(0,200):
        print getRandom(6)