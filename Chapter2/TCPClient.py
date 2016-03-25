import socket

target_host='127.0.0.1'
target_port=9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("hello world!")

response= client.recv(4096)

print response


# from socket import *


# HOST = 'localhost'
# PORT = 9999
# BUFSIZ = 1024
# ADDR = (HOST, PORT)

# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

# while True:
#     data = raw_input('> ')
#     if not data:
#         break
#     tcpCliSock.send(data)
#     data1 = tcpCliSock.recv(BUFSIZ)
#     if not data1:
#         break
#     print data1

# tcpCliSock.close()
