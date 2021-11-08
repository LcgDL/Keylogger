import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

while 1:
    m, d = s.recvfrom(1024)
    #print('Connection from: '+str(d)[19:24] + ' Mess: ' + m.decode())
    with open("example.txt", "a") as t:
        t.write(m.decode() + "\n")