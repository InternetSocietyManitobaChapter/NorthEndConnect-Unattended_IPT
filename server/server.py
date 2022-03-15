
# import socket programming library
import os
import csv
import json
import time
import socket
# import thread module
from _thread import *
import threading
 
csv_lock = threading.Lock()
 
# thread function
def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)

        if not data:
            print('Client disconnected')
             
            # lock released on exit
            csv_lock.release()
            break
        
        data = data.decode("utf-8")
        json_object = json.loads(data)
        
        version = (json_object["version"])
        hostname = (json_object["hostname"])
        ipv4 = (json_object["ipv4"])

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
 
    # connection closed
    c.close()
 
 
def Main():
    host = "127.0.0.1"
 
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 81
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        csv_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()