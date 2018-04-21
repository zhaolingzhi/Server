import socket
import json
import threading

end="END"
def detect(sock,addr):
    print "accept a new connection:%s:%s"% addr
    info={}
    info['sex']=1
    info['age']=3
    data = []
    count=1
    while True:
        print "recv"
        temp=sock.recv(8192)
        print "recv data %d"%count
        count+=1
        if end in temp:
            data.append(temp[:temp.find(end)])
            break
        data.append(temp)
    print len(data)


    sock.sendall(json.dumps(info))
    sock.close()
    print "connect from %s:%s closed"%addr

if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.1.103",8080))
    s.listen(5)
    print "start a server"
    while True:
        sock,addr=s.accept()
        print "get a connect"
        t=threading.Thread(target=detect,args=(sock,addr))
        t.start()
