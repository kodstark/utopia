import zmq
import sys

port = "5556"

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

print "Sending request "
socket.send ("Hello")
message = socket.recv()
print "Received reply ", "[", message, "]"    