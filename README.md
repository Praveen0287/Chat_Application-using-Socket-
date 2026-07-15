# Chat_Application-using-Socket-programming
Implementing a basic client-server chat application using sockets (TCP preferred)

## Features
- TCP Socket Programming
- Multi Client Support
- Real Time Messaging
- Broadcast Messages
- Username Support
- Graceful Client Disconnect
- Basic Error Handling
  
## Server Running
- Open the file where you wrote server code(i.e server.py) and open **Terminal1** and run **python server.py** then you will get displayed server running on 0.0.0.0:5000.
  
## Client Runninng
- Open the file where you wrote client code(i.e client.py) and open **Terminal2** and run **python client.py** then you will get displayed like
- Enter server IP:
- Enter Username:
- Give required IP(127.0.0.1) and username.
- Now open two or three new terminals and add client2 and client3.
- After adding new clients, you can see the new clients joined message in the server terminal and you can see the messages set by the clients in every client terminals.
  
## Assumptions
- Uses TCP sockets
- Maximum message size is 1024 bytes, we can adjust it.
- Multiple clients were handled by one server.
