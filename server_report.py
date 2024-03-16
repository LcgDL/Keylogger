# Import the socket module for network communication
import socket

# Create a socket object using IPv4 addressing (AF_INET) and UDP protocol (SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the local host ('') and a specified port number, making it listen on all available interfaces
s.bind(('', port))

# Start an infinite loop to continuously listen for incoming messages
while 1:
    # Receive data from the socket, up to 1024 bytes, and unpack it into message and address
    m, d = s.recvfrom(1024)
    
    # Uncomment the print statement below to display the connection details and message on the console
    #print('Connection from: '+str(d)[19:24] + ' Mess: ' + m.decode())
    
    # Open the file "example.txt" in append mode (or create it if it doesn't exist)
    with open("example.txt", "a") as t:
        # Write the decoded message to the file followed by a newline
        t.write(m.decode() + "\n")
