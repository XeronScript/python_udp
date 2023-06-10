import socket

# Adres IP grupy multicast
MULTICAST_GROUP = '224.0.0.1'
# Numer portu
PORT = 5000

# Tworzenie gniazda
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Wiązanie gniazda z adresem i portem
sock.bind(('0.0.0.0', PORT))

# Dodanie gniazda do grupy multicast
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0'))

while True:
    # Odbieranie danych
    data, address = sock.recvfrom(1024)
    message = data.decode()

    print(f'Otrzymano komunikat: {message} od {address}')

# Zamknięcie gniazda
sock.close()
