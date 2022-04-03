# A simple script to 
sudo apt update
sudo apt install docker-compose -y   # This will install all the requirements to run Docker VMs.
cd server
sudo docker-compose up -d    # The -d is for "detached" so they will run in the background and still allow use of the root OS.
