#!/usr/bin/python3

from argparse import ArgumentParser
from threading import Thread
from time import time
import socket

open_ports = []

# function to prepare arguments

def prepare_args():
	""" prepare arguments

		return :
			args(argparse.namespace)
	"""
	parser = ArgumentParser(description = "Python based Port scanner", usage ="%(prog)s IP", epilog="Example : %(prog)s -s 20 -e 1000 -t 500 -V 192.168.1.1")

	parser.add_argument(metavar = "IPV4", dest="ip", help = "host to scan")
	parser.add_argument("-s", "--start",metavar = "", dest="start", type = int, help ="starting port", default = 1)
	parser.add_argument("-e", "--end", metavar = "",dest="end", type = int, help ="ending port", default = 65535)
	parser.add_argument("-t", "--thread", metavar = "", dest="threads", type =int , help = "threads to use", default= 500)
	parser.add_argument("-V", "--verbose", dest="verbose", action = "store_true", help="verbose output")
	parser.add_argument("-v", "--version", action = "version" , version = "%(prog)s 1.0")

	args= parser.parse_args() 
	return args

# We use 'generators', when we use an element in a generator , then it is wiped from memory
# we also want a datatype which wipes the ports already beigned scanned


# Function to prepare ports
def prepare_ports(start:int , end:int):
	""" generator function
		
		arguments:
		start - starting port
		end	  - ending port
	"""

	for port in range(start, end+1):
		# 'yield' is similar to adding elemts in an array
		yield port

def scan_port():
	"""Scan ports
	"""

	while True :
		try :
			s = socket.socket()
			s.settimeout(1)
			# 'next' function to extract element from generator
			port = next(ports_to_scan)
			s.connect((arguments.ip , port))
			open_ports.append(port)
			if arguments.verbose :
				print(f"\r{open_ports}", end="")

		# Errors
		except (ConnectionRefusedError, socket.timeout):
			continue

		except StopIteration :
			break



# threading
def prepare_threads(threads: int) :
	""" Create , start and join threads

		arguments:
			threads(int) - Number of threads to scan
	"""

	# Lists for threads
	thread_list = []

	for _ in range(threads+1):
		
		# create a thread (using function )in the 'thread_list'
		thread_list.append(Thread(target= scan_port))

	for a in thread_list:
		a.start()

	# Join the threas to main thread i.e don't start the program until all threads are finished 
	for a in thread_list:
		a.join()


if __name__ == "__main__" :
	arguments = prepare_args()
	# generator variable 
	ports_to_scan = prepare_ports(arguments.start , arguments.end)
	start_time = time()
	prepare_threads(arguments.threads)
	end_time = time()
	if arguments.verbose :
		print()
	print(f"Open ports found - {open_ports}")
	print(f"Time taken - {round(end_time - start_time, 2)}")

# We are limited by no. of threads we can use.. 500 
# We have make sure that the no two threads are not scanning the same ports