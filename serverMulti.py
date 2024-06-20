from socket import *
import threading # In order to terminate the program


#Prepare a sever socket
def handleRequest(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename [1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n'.encode())
        #Send the content of the requested file to the client
        for i in range (0, len (outputdata)) :
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.close()
    
serverPort = 12000
serverSocket = socket (AF_INET, SOCK_STREAM)
serverSocket.bind (('127.0.0.1', serverPort))
serverSocket.listen(1)
print('The server is ready to receive.....')

while True:
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    print('Connection received from:', addr)
    threading.Thread(target = handleRequest, args = (connectionSocket, )).start()
serverSocket.close()