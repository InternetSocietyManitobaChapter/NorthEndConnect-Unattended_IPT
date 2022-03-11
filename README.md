# About this program
This program will sit in "C:\Program Files\Unattended IPT" of imaged computers.  
main.py will be turned into an exe using pyinstaller, with automatically generated settings and log files.  
It performs an automated test to Cira's Mini Internet Performance Test (performance.cira.ca/mini)  
It will also send the version, computer name, and ip address to a specified server running server.py  

# How to Opt out
To opt out of the program the user will have to go to "C:\Program Files\Unattended IPT"  
Open the settings.ini in a notepad  
Change "allow = YES" to "allow = NO" 

# Requirements to update the program
Windows  
Python 3.10  
PyInstaller  

# Turn Python script into an .exe application
pyinstaller --noconsole --onefile ./main.py