import socket

MULTICAST_GROUP = '224.0.0.1'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

# Dołączenie do grupy multicastowej
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0'))

while True:
    data, address = sock.recvfrom(1024)
    message = data.decode()
    print(f'Otrzymano komunikat: {message} od {address}')

sock.close()
