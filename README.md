# Unattended Performance Test
This program will sit in "C:\Program Files\Unattended IPT" of imaged computers.  
main.py will be turned into an exe using pyinstaller, with automatically generated settings and log files.  
It performs an automated test to Cira's Mini Internet Performance Test (performance.cira.ca/mini)  
It will also send the version, computer name, and ip address to a specified server running Server.py  

# How the program works
There are two Python files for this program.  
Main.py is for the client  
Server.py is for the server  

Main.py has variables for SERVER_ADDRESS and SERVER_PORT which need to be configured to match the Server.py host  
Server.py has the same SERVER_ADDRESS and SERVER_PORT variables, which need to be assigned  

Once those variables are set go into the client folder, and server folder respectively and run the following commands
```
Client Folder:  
pyinstaller --noconsole --onefile ./main.py  
  
Server Folder:  
pyinstaller ./server.py
```

Once the applications are built, grab the .exe from each of the respective build folders, and move them to the clients / server.  
## Client Application


## Server Application  
The server application build is not an all-in-one exe file like the client exe, as building it as an all in one flags it as a virus since an address and port are constantly being read  

# How to Opt out
To opt out of the program the user will have to go to "C:\Program Files\Unattended IPT"  
Open the settings.ini in a notepad  
Change "allow = YES" to "allow = NO"  

# Requirements to update the program
Windows  
Python 3.10  
PyInstaller  