#Allows network connections
import socket

def echo_client():
    host = 'localHost'
    port = 7200

    #AF_INET is the IPv4 address family
    #SOCK_STREAM is the TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as localSocket:
        #Connects to the server's IP and port
        localSocket.connect((host, port))
        print(f"Client connection made with server at {host} : {port}")

        while True:
            #Asks Client to input something and reads it
            message = input("Client enter message: ")

            #Message is encoded into bytes and sent to the server
            localSocket.sendall(message.encode('utf-8'))

            #Awaits server's response and decodes back to string for printing
            response = localSocket.recv(1024).decode('utf-8')
            print(f"Client received: {response}")

            #If user were to type "end" and received "dne" then the loop is exited and closes
            if message.lower() == 'end' and response.lower() == 'dne':
                print("Client termination called by message \"end\" and response \"dne\"")
                break

if __name__ == "__main__":
    echo_client()

