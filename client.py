import sys
from socket import *
import threading

if len(sys.argv) < 4:
    print("Enter like this: Client.py localhost serverPort filename1 [filename2 ...]")
    sys.exit()

serverIPAddress = sys.argv[1]         
serverPort = int(sys.argv[2])    
fileList = sys.argv[3:]         

def request_file(filename):
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverIPAddress, serverPort))

        httpRequest = f"GET /{filename} HTTP/1.1\r\nHost: {serverIPAddress}\r\n\r\n"
        print("HTTP Request being sent:\n", httpRequest)
        clientSocket.send(httpRequest.encode())

        serverResponse = ""
        while True:
            dataChunk = clientSocket.recv(1024).decode()
            if not dataChunk:
                break
            serverResponse += dataChunk

        print(f"\nResponse for {filename}:\n", serverResponse)

    except Exception as e:
        print(f"Error requesting {filename}: {e}")

    finally:
        clientSocket.close()

threadList = []
for filename in fileList:
    thread = threading.Thread(target=request_file, args=(filename,))
    threadList.append(thread)
    thread.start()
    
for thread in threadList:
    thread.join()
