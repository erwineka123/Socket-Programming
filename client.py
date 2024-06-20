import socket
import sys

def httpClient(serverHost, serverPort, path):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((serverHost, serverPort))

    # Send HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {serverHost}\r\nConnection: close\r\n\r\n"
    client_socket.sendall(request.encode())

    # Receive response from the server
    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

    # Close the connection
    client_socket.close()

    # Print the response
    print(response.decode())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <serverHost> <serverPort> <path>")
        sys.exit(1)

    serverHost = sys.argv[1]
    serverPort = int(sys.argv[2])
    path = sys.argv[3]

    httpClient(serverHost, serverPort, path)