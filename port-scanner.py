#!/usr/bin/python3

import sys
import socket

# Default checking - if not present in stderr
if len(sys.argv) == 1 :
	print(f"[USAGE]: {sys.argv[0]} IP START(optional) END(optional)", file = sys.stderr)
	exit(1)

# Checking if he provided both the arguments
ip = sys.argv[1]
start = 1
end = 65535

if len(sys.argv) >= 3 :
	start = int(sys.argv[2])
	# if length is more than 3
	if len(sys.argv) >= 4 :
		end = int(sys.argv[3])


# Function for checking port status 
		# '->' is used for showing the returnType 

def check_port_status(port:int) -> bool :
	# Usign 'try' , since we'll get too man erros
	try:
		s = socket.socket()
		s.settimeout(1)
		s.connect((ip,port))
		return True

	# If there are errors then return 'false'
	except (ConnectionRefusedError , socket.timeout) :
		return False

# Scanning through every port by - loop

for port in range(start,end):
	response = check_port_status(port)
	if response:
		print(f"Open port found [{port}]")


## This is not a time efficient port scanner , scans 1 port at a time in 1s ... to slow on a LAN or WAN

