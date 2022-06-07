
import socket

server=socket.socket()
server.connect(('localhost',1002))
file=open("test.png","rb")
image_data=file.read(2048)
while image_data:
    server.send(image_data)
    image_data=file.read(2048)
file.close()
server.close()
