import zmq
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:

    
    
    msg = socket.recv()
    print "Received: ", msg

    print "Send: world!"
    socket.send("world!")
    time.sleep(1)