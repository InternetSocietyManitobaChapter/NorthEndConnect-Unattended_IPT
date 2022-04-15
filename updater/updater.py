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
# Supported with funding from the Internet Society Manitoba Chapter Inc. (www.internetsocietymanitoba.ca) 

# Top level variables to change depending on requirements
TCP_IP = "192.168.1.102"
TCP_PORT = 81
BUFFER_SIZE = 1024

# IMPORTS
import os
import shutil
import time
import subprocess
import json
import socket
import zipfile
from configparser import ConfigParser
# END OF IMPORT.

# Initialize the config parser    
config = ConfigParser()
config.read('settings.ini')

# Main functions
if not config.has_option('settings', 'version'):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        version = {'version': "0",'hostname': "",'ipv4': ""}
        data = json.dumps(version)
        s.sendall(bytes(data, encoding="utf-8"))

        if(os.path.isdir('UPT')):
            shutil.rmtree('UPT')

        os.mkdir('UPT')

        with open('UPT.zip', 'wb') as f:
            while True:
                data = s.recv(BUFFER_SIZE)
                if not data:
                    f.close()
                    break
                f.write(data)

        s.close()
        
        with zipfile.ZipFile('UPT.zip', 'r') as zip_ref:
            zip_ref.extractall('UPT')

        print('version unmatched')
        subprocess.run([r"UPT/UPT.exe"])
    except:
        print('Connection failed w/o Settings')
else:
    try:
        VERSION = config.get('settings', 'version')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        version = {'version': VERSION,'hostname': "",'ipv4': ""}
        data = json.dumps(version)
        s.sendall(bytes(data, encoding="utf-8"))

        check = s.recv(1024)

        if check != b"DONE":
            if(os.path.isdir('UPT')):
                shutil.rmtree('UPT')

            os.mkdir('UPT')

            with open('UPT.zip', 'wb') as f:
                while True:
                    data = s.recv(BUFFER_SIZE)
                    if not data:
                        f.close()
                        break
                    f.write(data)

            s.close()
            
            with zipfile.ZipFile('UPT.zip', 'r') as zip_ref:
                zip_ref.extractall('UPT')

            print('version unmatched')
            subprocess.run([r"UPT/UPT.exe"])
        else: 
            subprocess.run([r"UPT/UPT.exe"])
    except:
        print('Connection failed w/ Settings')
