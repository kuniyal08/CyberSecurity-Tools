#! /bin/python3

import sys  # module that lets us enter command line arguments and other utils
import socket
from datetime import datetime

# Defining the target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 Network-PortScanner.py <ip>")
    sys.exit()

# Add a banner
print("-" * 50)
print("Scanning Target " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 70)
# asdadssa
