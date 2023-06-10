import socket

PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('0.0.0.0', PORT))

while True:
    data, address = sock.recvfrom(1024)
    message = data.decode()
    print(f'Otrzymano komunikat: {message} od {address}')

sock.close()
