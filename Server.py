#Allows network connections
import socket

def reverseEchoServer():
    port = 7200
    #Accepts connections from any IP
    host = '0.0.0.0'
#AF_INET is the IPv4 address family
#SOCK_STREAM is the TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        #Attaches the server to the port and the IP address
        serverSocket.bind((host, port))

        #Allows only 1 connection at a time
        serverSocket.listen(1)
        print(f"Server can now receive from port {port}")

        #clientSocket is the new socket for communicating with client
        #clientAddress is IP address of client
        clientSocket, clientAddress = serverSocket.accept()

        print(f"Server connection made with client {clientAddress}")

        #Uses clientSocket to communicate
        with clientSocket:

            while True:
                #Receives data from client and decodes
                data = clientSocket.recv(1024).decode('utf-8')

                #Prints what is sent by client
                print(f"Server received: {data}")

                #Python shortcut is used to reverse string
                reversedData = data[::-1]

                #Turns data into bytes and sends reversed string back to the client
                clientSocket.sendall(reversedData.encode('utf-8'))

                #Prints reversed message back
                print(f"Server sent: {reversedData}")

                #When "end" is received by the server, loop is broken and terminates
                if data.lower() == 'end':
                    print("Server termination called by \"end\"")
                    break

if __name__ == "__main__":
    reverseEchoServer()
