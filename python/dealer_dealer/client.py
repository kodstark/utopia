import zmq
import random
import sys
import time

def _urlsForMasks():
    masks = [
        "192.168.43.*",
        "10.20.6.*",
    ]
    for mask in masks:
        for ipPart in range(1, 254):
            for port in range(5590, 5600):
                ip = mask.replace("*", str(ipPart))
                yield "tcp://%s:%s" % (ip, port)

context = zmq.Context()
poller = zmq.Poller()

socket = context.socket(zmq.DEALER)
poller.register(socket, zmq.POLLIN)

for url in _urlsForMasks():    
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