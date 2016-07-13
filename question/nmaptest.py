# coding:utf-8
import optparse
import nmap
import socket


def nmapScan(tgtHost, tgtPort):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
        print tgtIP
    except:
        print "[+] unkown host"
        return
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    state = results['scan'][tgtIP]['tcp'][int(tgtPort)]['state']
    print ("[*]" + tgtHost + " tcp/" + tgtPort + " " + state)

if __name__ == "__main__":
    print "here"
    nmapScan("www.baidu.com", "80")
