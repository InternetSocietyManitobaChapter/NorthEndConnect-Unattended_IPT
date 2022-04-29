# A simple script to install everything

# Update package manager (apt-get) 
# and install (with the yes flag `-y`)
# Python and Pip 
apt-get update && apt-get upgrade && apt autoremove -y
apt-get install python3.8 -y
apt-get install python3-pip -y

# Install other Python dependencies
pip3 install Requests Pygments
pip3 install selenium
pip3 install webdriver-manager
python3 -m pip install -U nuitka
pip3 install psutil
pip3 install subprocess.run

#Compile the "main.py" python code into UPT.exe
cd client
python3 -m nuitka --windows-disable-console -o UPT.exe main.py

#ZIP the files and move them to the /server folder
apt install zip -y
zip -r UPT.zip *
cp UPT.zip ../server

#Compile the python code for the Updater.exe
cd ../updater
python3 -m nuitka --windows-disable-console -o updater.exe updater.py
zip -r updater.zip *

#Compile the python code for the "CIRA only" test
cd ../CIRA
python3 -m nuitka --windows-disable-console -o cira.exe cira.py
zip -r cira.zip *

# Run the script to start listening for connections

cd ../server
#chmod +x server.py
#python3 server.py
nohup python3 -u server.py > output.log &
