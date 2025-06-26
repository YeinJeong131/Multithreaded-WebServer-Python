#import socket module
from socket import *
import sys  # In order to terminate the program
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
serverPort = 56565
serverSocket.bind(('’, serverPort))
serverSocket.listen(5)
print("Ready to serve...")

# Function to handle client requests
def handle_client(individualSocket):
    try:
        # Receive the request message from the client
        message = individualSocket.recv(1024).decode()

        print("Request message: ", message)

        filename = message.split()[1]

        print("Requested filename: ", filename)

        # Open the requested file
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        individualSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            individualSocket.send(outputdata[i].encode())

        individualSocket.send("\r\n".encode())

    except IOError:
        # Send response message for file not found
        individualSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        individualSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    
    finally:
        # Close client socket
        individualSocket.close()

# Main server loop
while True:
    # Establish the connection
    individualSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    # Create a new thread to handle the client's request
    client_thread = threading.Thread(target=handle_client, args=(individualSocket,))
    client_thread.start()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data

