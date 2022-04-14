# A simple script to install everything
sudo apt update 

# Update package manager (apt-get) 
# and install (with the yes flag `-y`)
# Python and Pip
apt-get update && apt-get install -y \
    python3.8 \
    python3-pip

# Install our Python dependencies
pip install Requests Pygments

# Run the script when the image is run
# ["python3", "/home/server.py"]
