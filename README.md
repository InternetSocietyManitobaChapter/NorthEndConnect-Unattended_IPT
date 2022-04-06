# Unattended Performance Test
This program was built to be used in the Northend Project of the Internet Society of Manitoba Chapter.  
It connects the computer to the Internet Society's server, as well as CIRA's Mini Performance Test.  
Cira.py is the standalone performance test, and only the performance test.  

Main.py is the performance test, which also sends info to the server.  
Updater.py is the self updater for the main runner, which extracts the updated ZIP from the server.  
Server.py is the server itself, it will receive information to put into a server_logs folder, as well as send UPT.zip to clients that require an update.  

# Requirements
Python 3.10  
Python PIP  
Python Nuitka | https://github.com/Nuitka/Nuitka 
Python PyInstaller | https://pyinstaller.readthedocs.io/en/stable/index.html  
  
# Basic Configuration Information
Updater, Client, and Server python files have a TCP_IP and TCP_PORT that will need to be adjusted to the server that server.py resides on.  
Main and Server python files have a version setting, you will need to adjust that if there are any updates required.  

# Commands & Setup
For CIRA only test
python -m nuitka --windows-disable-console cira.py

In Updater Folder  
python -m nuitka --windows-disable-console updater.py  
Put updater.build, updater.cmd and updater.exe in a Zip for distribution

In Client Folder  
python -m nuitka --windows-disable-console -o UPT.exe main.py  
This command will take some time to run  
ZIP the main.build, main.cmd and UPT.exe into a ZIP file called UPT.zip
Move the UPT.zip to the same folder as the Server.py

In Server Folder
Use in Linux, requires Python 3.10  
Change version, or update information as required in the server.py  
Make sure UPT.zip is the most recently updated build of Main.py

# Licensing
Copyright [2022] [Allen Padilla]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.