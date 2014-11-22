var zmq = require('zmq')
    , sock = zmq.socket('pair');

sock.connect('tcp://192.168.1.3:5556');

setInterval(function(){
    console.log('sending hello');
    sock.send('hello world');
}, 10);
