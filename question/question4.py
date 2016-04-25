# coding:utf-8

import MySQLdb
from question2 import getRandom

def connect():
    try:
        con = MySQLdb.connect(host='localhost',
                              user='root',
                              passwd='',
                              db='temp',
                              port=3306)
        cur = con.cursor()
        # items = cur.execute("select * from tbl")
        value = "222"
        items = cur.execute('insert into tbl (code) values ("%s")'%value)
        print items
        con.commit()
        cur.close()
        con.close()
    except MySQLdb.Error, e:
        print e

def connectdatabase(function):
    try:
        con = MySQLdb.connect(host='localhost',
                              user='root',
                              passwd='',
                              db='temp',
                              port=3306)
        cur = con.cursor()
        # items = cur.execute("select * from tbl")
        # value = "222"
        # items = cur.execute('insert into tbl (code) values ("%s")'%value)
        # print items
        function(cur)
        con.commit()
        cur.close()
        con.close()
    except MySQLdb.Error, e:
        print e



def showcode(cur):
    mysqlShell = 'select * from tbl'
    items = cur.execute(mysqlShell)
    # for item in items:
    #     print item
    print items
    pass

def getCode(num):
    apps = []
    for i in range(num):
        apps.append(getRandom(6))
    return apps

def addcode(cur):
    apps = getCode(6)

    for item in apps:
        mysqlShell = 'insert into tbl (code) values ("%s")' % item
        items = cur.execute(mysqlShell)
        print items

    pass

def addcodes(cur):
    apps = getCode(6)
    print apps
    apps  = [('asdsad','asdasds')]
    # apps = set(apps)
    # print apps
    mysqlShell = 'insert into tbl (code) values (%s)'
    items = cur.executemany(mysqlShell,apps)
    print items



if __name__ == '__main__':
    # showcode()
    # print getCode(6)
    connectdatabase(addcodes)