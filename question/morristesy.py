# coding:utf-8
import optparse
import socket
import threading

screenLock = threading.Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        result = connSkt.recv(100)
        screenLock.acquire()
        print ('[+]%d/tcp open'% tgtPort)
        print ("[+]"+str(result))
    except:
        screenLock.acquire()
        print ('[+]%d/tcp close'% tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s':Unknown host" %tgtHost
        return 
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print ('\n[+] Scan Results for:'+tgtName[0])
    except:
        print ('\n[+] Scan Results for:'+tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print ('Scanning port '+str(tgtPort))
        connScan(tgtHost,int(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    # parser = optparse.OptionParser('usage%prog -H <targethost> -p <target port>')
    # parser.add_option('-H',dest='tgtHost', type='string',help='specify target host')
    # parser.add_option('-p',dest='tgtPort', type='int',help='specify target port')
    # (options,args) = parser.parse_args()
    # tgtHost = options.tgtHost
    # tgtPort = options.tgtPort
    # if (tgtHost == None)|(tgtPort == None):
    #     print parser.usage
    #     print "here"
    #     exit(0)
    # else:
        # print tgtHost
        # print tgtPort
    # portScan(tgtHost,tgtPort)
    portScan('www.qq.com', [80,443,3389,1433,23,445])

if __name__=='__main__':
    main()
        

    
