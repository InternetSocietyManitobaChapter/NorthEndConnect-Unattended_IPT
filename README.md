# Unattended Performance Test
This program was built to be used in the North End Connect Project of the Internet Society of Manitoba Chapter.
It connects the computer to the Internet Society's server, as well as remotely triggering the Canadian Internet Registration Authority (CIRA)'s Mini Performance Test (part of the Internet Performance Test (IPT) https://performance.cira.ca/ or the low bandwidth version https://performance.cira.ca/mini/ ).

There are 4 areas within this software. "Cira.py" works by itself and all it does is silently run CIRA's IPT from a Windows 10 client computer. The other option required parts 2, 3 & 4 running on the Win 10 clients, in partnership with a Ubuntu server avaialbe somewhere on the open internet.

  1) Cira.py is the standalone performance test, and only the performance test.  

  2) Main.py is the performance test, which also sends info to the server.

  3) Updater.py is the self updater for the main runner, which extracts the updated ZIP from the server.

  4) Server.py is the server itself, it will receive information to put into a server_logs folder, as well as send UPT.zip to clients that require an update.  

# Paths
The Win 10 client requires the following software in these paths: folder/files


# Requirements
Python 3.10  
Python PIP  
Python Nuitka | https://github.com/Nuitka/Nuitka 
Python PyInstaller | https://pyinstaller.readthedocs.io/en/stable/index.html  
  
# Preparation

# Windows 10 Client Prep
On a clean windows 10 installation, Python and Nuitka will need to be installed

For the Stable version use the following command (https://nuitka.net/doc/download.html):
python3 -m pip install -U nuitka

# Copy the project files:


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

# Windows Task Scheduler
Create a new basic task in Task Scheduler, on start up pointing at the Updater.exe file
Open the properties of the task, and go to triggers
Delay tasks for a random amount of time after start up

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
