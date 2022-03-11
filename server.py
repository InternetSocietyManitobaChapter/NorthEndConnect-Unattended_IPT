import csv
import os
import json
import time
import socket

# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to server address and port 81
server_address = ('localhost', 81)
tcp_socket.bind(server_address)
 
# Listen on port 81
tcp_socket.listen(1)
 
while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
 
    try:
        print("Connected to client IP: {}".format(client))
         
        # Receive and print data 32 bytes at a time, as long as the client is sending something
        while True:
            data = connection.recv(1024)
            data = data.decode("utf-8")
            json_object = json.loads(data)
            
            version = (json_object["version"])
            hostname = (json_object["hostname"])
            ipv4 = (json_object["ipv4"])

            csvName = f'{time.strftime("%Y-%m-%d")}.csv'

            if os.path.exists(csvName):
                with open(csvName, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([version,hostname,ipv4])
                    break
            else:
                with open(csvName, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(json_object)
                    writer.writerow([version,hostname,ipv4])
                    break

            if not data:
                break
 
    finally:
        connection.close()