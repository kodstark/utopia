import sys
import zmq

url = "tcp://*:5556"

context = zmq.Context()
socket = context.socket(zmq.REP)
print "Listed on: ", url
socket.bind(url)

message = socket.recv()
print "Received request: ", message

secret = "kd_secret"
print 'Sending secret...'
socket.send(secret)