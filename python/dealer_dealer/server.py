import sys
import zmq

url = "tcp://192.168.43.55:5580"

context = zmq.Context()
socket = context.socket(zmq.DEALER)
print "Listed on: ", url
socket.bind(url)

secret = "kd_secret"
print 'Sending secret when somebody connects...'
socket.send(secret)