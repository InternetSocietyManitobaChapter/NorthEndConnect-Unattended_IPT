# A simple script to install everything
sudo apt update

# This will install all the requirements to run Docker VMs.
sudo apt install docker-compose -y  

# Move to the directory with the docker-compose and supporting files.
cd server

# The -d is for "detached" so they will run in the background and still allow use of the root OS.
# The --build will force a fresh build in case this is not the first time the install process has been attempted.
sudo docker-compose up -d --build
