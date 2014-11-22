var zmq = require('zmq')
    , sock = zmq.socket('pair');

sock.bind('tcp://*:5556');

sock.on('message',function(data){
    console.log("Data received : " + data.toString());
    sock.send("Echo hello")
});