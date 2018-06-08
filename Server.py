import socket
import json
import threading
import demjson
import base64
import matplotlib.pyplot as plt
import Image
import StringIO
from detector import Detector

end="END"

def detect(sock,addr):
    print "accept a new connection:%s:%s"% addr
    info={}
    data = []
    while True:
        temp=sock.recv(8192)
        if end in temp:
            data.append(temp[:temp.find(end)])
            break
        data.append(temp)
    StringDate=''
    for each in data:
        StringDate+=each
    JsonDate=demjson.decode(StringDate)
    imageString=JsonDate['image']
    image=Image.open(StringIO.StringIO(base64.b64decode(imageString)))

    info['gender'],info['age']=mDetector.predict(image)
    sock.sendall(json.dumps(info))
    sock.close()
    print "connect from %s:%s closed"%addr


if __name__=="__main__":

    mDetector= Detector()

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.43.239",8080)) #192.168.43.239
    s.listen(5)
    print "start a server"
    while True:
        sock,addr=s.accept()
        print "get a connect"
        t=threading.Thread(target=detect,args=(sock,addr))
        t.start()
