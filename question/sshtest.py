# coding:utf-8

import pexpect
PROMPT = ['#', '>>>', '>', '\$']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before


def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    # child.expect(PROMPT)
    # child.sendline("ls")
    # print child.before
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print "[-] Error Connecting ret"
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret == 0:
        print "[-] Error Connecting"
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = "192.168.0.98"
    user = 'user'
    password = "pass"
    child = connect(user, host, password)
    if child:
        send_command(child, 'cat /etc/shadow | grep root')
    else:
        print "error"

if __name__ == "__main__":
    main()
