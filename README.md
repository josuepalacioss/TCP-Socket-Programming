# TCP-Socket-Programming
TCP Socket Programming – Reverse Echo Server and Client Course: This project demonstrates a client-server communication system implemented in Python using TCP sockets. The goal was to establish reliable two-way communication over a network using TCP, focusing on connection handling, message exchange, and string manipulation.

Project Overview
Built a Reverse Echo Server that receives messages from a client and returns them in reverse order.

Developed a Client application that sends user-inputted messages to the server and displays the reversed response.

The server and client run on separate terminals and communicate via TCP on port 7200.

Program terminates cleanly when the user sends "end", with the server returning "dne".

Key Features
  Socket programming using Python’s socket library.

  Support for dynamic IP (0.0.0.0) to allow connections from any address.

  String reversal logic handled by the server before sending responses.

  Loop-driven message exchange until a termination keyword is detected.

Learning Outcomes
  Gained practical experience in TCP socket creation, binding, listening, and accepting connections.

  Understood client-server architecture and message protocols.

  Learned how to build stateful connections and manage byte-string encoding and decoding.
