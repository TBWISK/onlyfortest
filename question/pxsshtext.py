# coding:utf-8
from pexpect import pxssh
import optparse
import time
import threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print (s.before)


def connect(host, user, password, release):
    global Found, Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print ("[+] Password Found:" + password)
        Found = True
        return s
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()
        # print "[-] Error Connecting"
        # exit(0)


def main():
    """
    缺一个多扫描的线程
    """
    connection_lock.acquire()
    s = connect('192.168.0.98', 'user', 'passwor', True)
    send_command(s, 'ls')
main()
