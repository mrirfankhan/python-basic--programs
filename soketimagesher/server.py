import socket

server=socket.socket()
server.bind(('localhost',1002))
server.listen(5)
clint_socket,clint_addres=server.accept()
file=open("hack.png","wb")
image_chunk=server.recv(2048)
while image_chunk:
    file.write(image_chunk)
    image_chunk=server.recv(2048)
file.close()
server.close()
