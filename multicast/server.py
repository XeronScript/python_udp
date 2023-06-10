import socket

MULTICAST_GROUP = '224.0.0.1'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

while True:
    message = input("Wpisz wiadomość: ")
    sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))

sock.close()
