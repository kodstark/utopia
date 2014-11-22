import zmq
import random
import sys
import time

def _urls():
	for ip in range(10, 60):
		for port in range(5500, 5600):
			yield "tcp://192.168.43.%s:%s" % (ip, port)

context = zmq.Context()
poller = zmq.Poller()

socket = context.socket(zmq.DEALER)
poller.register(socket, zmq.POLLIN)

for url in _urls():    
    print 'Connect for %s' % url
    socket.connect(url)     


print 'Polling for all connected URLs'

while True:
    socketsPairs = poller.poll()
    for socketPair in socketsPairs:
        socket = socketPair[0]
        secret = socket.recv()
        print 'Got secret', secret
    time.sleep(1) 

    


