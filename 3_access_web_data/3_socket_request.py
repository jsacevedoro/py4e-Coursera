"""You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers."""

import socket 

# Create the socket object, first argument is the adress family and the second isthe socket type which is TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connect to the domain in the port 80, the correct port for http protocol
sock.connect(('data.pr4e.org', 80))

# Create request and turno into the right format
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)

while True:
    # Receives up to 512 bytes of data
    data = sock.recv(512)
    # This line checks if the length of the received data is less than 1 byte
    if len(data) < 1:
        break
    print(data.decode(), end = '')

sock.close()