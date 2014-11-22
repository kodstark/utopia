import zmq
import random
import sys
import time

from zmq import Poller

def _urls():
    return ["tcp://localhost:%s" % port for port in range(5500, 5600)]

context = zmq.Context()
poller = Poller()

# one socket, multiple connections

# socket = context.socket(zmq.REQ)
# poller.register(socket, zmq.POLLIN)

for url in _urls():    
    print 'Connect for %s' % url
    socket = context.socket(zmq.REQ)
    socket.connect(url)  
    poller.register(socket, zmq.POLLIN)
    socket.send("Hello")

while True:
    socketsPairs = poller.poll()
    for socketPair in socketsPairs:
        socket = socketPair[0]
        secret = socket.recv()
        print 'Got secret', secret
    time.sleep(1) 

    


