import sys
import zmq

url = "tcp://*:5556"

context = zmq.Context()
socket = context.socket(zmq.DEALER)
print "Listed on: ", url
socket.bind(url)

secret = "kd_secret"
print 'Sending secret...'
socket.send(secret)