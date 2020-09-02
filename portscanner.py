#! /usr/bin/env python3

# This is an intro to python lab to create a port scanner
# similar to nmap


# Import modules
import socket
import sys
from datetime import datetime

# User input: IP, Port
ipToTest = input("\nWhat IP would you like to scan?\n\n")
portToTest = socket.gethostbyname(ipToTest)

# Making the program look prettier
print("\n\nScanning host", portToTest)


# variable reservation 
#addrtype = input("\nIPV4 or IPV6?\n\n")
# variable reservation

# Set first time variable
dtstart = datetime.now()
try:
    for portToTest in range(1,1025):
        # IPV4 socket with TCP connections
        jsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = jsock.connect_ex((ipToTest,portToTest))
        if result == 0:
            print("Port " + str(portToTest) + " Open")
        jsock.close()
    while portToTest not in range(0,1025):
        print("Port " + (portToTest) + " must be between 1-1024")
except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    print("IP hostname not resolved. Please try again.")
    sys.exit()
except socket.error:
    print("Could not connect.")
    sys.exit()
    
# Set second time and calculate total time to scan
dtend = datetime.now()
time = dtend - dtstart
print("This scan completed in: ", time)
