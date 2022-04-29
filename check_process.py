#def check_process():
#    import subprocess
#   import urllib3
#    script_name = "server.py"
#    cmd='pgrep -f .*python.*{}'.format(script_name)
#    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    my_pid, err = process.communicate()
#    if len(my_pid.splitlines()) >0:
#        print("Script Running in background")
        #sys.exit(0);
#check_process()

#def check_script_status():
import subprocess
    
pytonProcess = subprocess.check_call("ps -ef | grep server.py",shell=True).decode()
pytonProcess = pytonProcess.split('\n')
  
for process in pytonProcess:
    print(process)

#check_script_status()
