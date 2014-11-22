import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)


while True:
	print "Sending Hello"
	socket.send("Hello")

	msg = socket.recv()
	print "Received:", msg

	time.sleep(1)