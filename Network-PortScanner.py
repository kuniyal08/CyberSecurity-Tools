#! /bin/python3

import sys  # module that lets us enter command line arguments and other utils
import socket
from datetime import datetime

# Defining the target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments. ")
    print("Syntax: python3 Network-PortScanner.py <ip>")
    sys.exit()

# Add a banner
print("-" * 50)
print("Scanning Target " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # AF_INET is IPV4 SOCK_STREAM is the Port
        socket.setdefaulttimeout(1)  # is a float i.e can be .5
        result = s.connect_ex(
            (target, port)
        )  # returns error indicator. If no error will return 0
        print("Checking the port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program. ")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. ")
    sys.exit()
