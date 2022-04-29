import psutil

def checkIfProcessRunning(processName):

    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# Check if any chrome process was running or not.
if checkIfProcessRunning('python.py'):
    print('Yes a chrome process was running')
else:
    print('No chrome process was running')

def check_script_status():
        import subprocess
    
        pytonProcess = subprocess.check_output("ps -ef | grep server.py",shell=True).decode()
        pytonProcess = pytonProcess.split('\n')
  
        for process in pytonProcess:
                print(process)

#check_script_status()
