#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Install ajihunter command
sudo cp ajihunter.py /usr/local/bin/ajihunter
sudo chmod +x /usr/local/bin/ajihunter
echo "ajihunter has been installed and is now available as a command."

# Automatically run ajihunter -h
ajihunter -h
