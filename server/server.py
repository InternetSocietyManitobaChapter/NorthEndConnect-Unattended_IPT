from asyncio.windows_events import NULL
import os
import csv
import time
import json
import socket
from threading import Thread
from socketserver import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 81
BUFFER_SIZE = 1024

filename='UPT.exe'
VERSION="1"

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print (" New thread started for "+ip+":"+str(port))

    def run(self):
        data = self.sock.recv(1024)        
        data = data.decode("utf-8")
        json_object = json.loads(data)
        
        version = json_object["version"]

        if version == VERSION:
            hostname = json_object["hostname"]
            ipv4 = json_object["ipv4"]
            csvName = f'./server_logs/{time.strftime("%Y-%m-%d")}.csv'

            if os.path.exists(csvName):
                with open(csvName, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([version,hostname,ipv4])
            else:
                if not os.path.exists('server_logs'):
                    os.makedirs('server_logs')

                with open(csvName, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(json_object)
                    writer.writerow([version,hostname,ipv4])
                    
            self.sock.send(b"DONE")
            self.sock.close()
        else:
            f = open(filename,'rb')
            
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    #print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(10)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
