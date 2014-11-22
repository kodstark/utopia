import zmq
import random
import sys
import time

from zmq import Poller

def _urls():
    return ["tcp://localhost:%s" % port for port in range(5500, 5600)]

context = zmq.Context()
poller = Poller()

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

    

