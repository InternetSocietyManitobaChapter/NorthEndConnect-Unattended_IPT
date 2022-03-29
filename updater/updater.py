# Copyright 2022 Allen Padilla
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Supported with fundamental from the Internet Society Manitoba Chapter Inc. (www.internetsocietymanitoba.ca) 

# Top level variables to change depending on requirements
SERVER_ADDRESS="localhost"
SERVER_PORT=81
WAIT_TIME=300

# IMPORTS
import subprocess
import json
import socket

from configparser import ConfigParser
# END OF IMPORT

TCP_IP = 'localhost'
TCP_PORT = 81
BUFFER_SIZE = 1024

# Initialize the config parser    
config = ConfigParser()
config.read('settings.ini')

# Main functions
if not config.has_option('settings', 'version'):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        version = {'version': '0'}
        data = json.dumps(version)
        s.sendall(bytes(data, encoding="utf-8"))

        with open('UPT.exe', 'wb') as f:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        s.close()
        print('version unmatched')
        subprocess.run([r"UPT.exe"])
    except:
        print('Connection failed')
else:
    try:
        VERSION = config.get('settings', 'version')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        version = {'version': VERSION}
        data = json.dumps(version)
        s.sendall(bytes(data, encoding="utf-8"))

        check = s.recv(1024)

        if check != b"DONE":
            with open('UPT.exe', 'wb') as f:
                while True:
                    #print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    if not data:
                        f.close()
                        break
                    # write data to a file
                    f.write(data)

        s.close()
        print('version match')
        subprocess.run([r"UPT.exe"])
    except:
        print('Connection failed')