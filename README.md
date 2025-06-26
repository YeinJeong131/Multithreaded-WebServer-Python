# NF_ProjectA - Multithreaded Web Server and Client in Python

This project demonstrates the implementation of a **multithreaded web server** and a **client** using Python's socket and threading modules. It was completed as part of a networking assignment.

## 📁 Project Structure
NF_ProjectA/ <br/>
│ <br/>
├── Server.py # Multithreaded web server code <br/>
├── Client.py # Client code for requesting files <br/> 
├── HelloWorld.html # Example HTML file to be requested <br/>
├── Test.html # Another example file <br/> 
└── README.md # Project documentation <br/>

## 🚀 How to Run

### 1. Start the Server

```bash
python Server.py
```
You will see:
```bash
Ready to serve...
```
### 2. Run the Client in a separate terminal
```bash
python Client.py localhost 56565 HelloWorld.html Test.html
```
This sends multiple requests using multithreading to the server.
> Make sure to use the same port number (e.g. 56565) in both server and client.

## 🔍 Key Concepts Learned
- bind() vs connect():
  - bind() is used on the server to specify its address/port.
  - connect() is used on the client to connect to the server.
- Port number choice:
  - Ports below 1024 are reserved; used 56565 for testing as it's above 1024.
- Multithreading (threading.Thread):
  Used to handle multiple client requests simultaneously.
- Loopback Address (127.0.0.1):
  Used for local testing without external network access.
  
## 🧠 Issues Resolved
- Confusion about using bind() and connect().
- Correctly constructing the HTTP GET request message.
- Encountered errors due to missing Python path → solved by setting the proper environment variable.
- Understood why the server listens on 127.0.0.1 instead of the device IP.


