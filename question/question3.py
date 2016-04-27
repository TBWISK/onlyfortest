# coding:utf-8
import redis

def connet():
    print redis.__file__
    r = redis.Redis(host='localhost',port=6379,db=1)
    # info = r.info()
    # r.save("222")
    r.set(22,22)

    r.get(22)
    # for key in info:
        # print '%s:%s' %(key,info[key])
    # print info

connet()
