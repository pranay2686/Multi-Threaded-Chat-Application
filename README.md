# Multi-Threaded-Chat-Application
A multithreaded Python chat application using sockets that allows multiple clients to send and receive messages concurrently.

This is a simple terminal-based chat application built using Python's "socket" and "threading" modules. It demonstrates how to build a real-time client-server architecture where multiple users can chat concurrently.

## :link:Features
- **Multithreaded Server** : Handles multiple clients simultaneously using threads.
- **Private Messaging** : Send messages directly to a specific user using "@nickname: "your message".
- **Broadcast Messaging** : All other messages are sent to every connected user.
- **Client-Server Architecture** : Classic socket programming in Python.
- **Graceful Exit** : Users can disconnect cleanly using "Ctrl+C" or typing "exit".

## :link:Run the Server
    python server.py 
   
 **You’ll see:** <br>
         Server started!<br>
         IP: 127.0.0.1 <br>
         Port: 12341 <br>
         Waiting for clients...

## :link:Run the Client (in a new terminal)
    python client.py<br>
     
   **Provide:**<br>
        Server IP → localhost<br>
        Port → 12341<br>
        Nickname → your chat name<br>
        Repeat for multiple clients in separate terminals to simulate a group chat.

## :link:Private Messaging Format
   Use this format to send a direct message to another user: <br>
     @nickname: "your message".
    
    

