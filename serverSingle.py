from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#preapare a server socket
serverPort = 12000 
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)
print('The server is ready to receive......')

while True:
    #establish the connection
    connectionSocket, adr = serverSocket.accept()
    print('Connection received from:', adr)
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read() 
    
        #send HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        #send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #send respinse message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        #close client socket
        connectionSocket.close()
    
serverSocket.close()
sys.exit()