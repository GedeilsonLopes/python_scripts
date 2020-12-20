import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('w3.org', 80))
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\n\n'.encode()

my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
my_sock.close()