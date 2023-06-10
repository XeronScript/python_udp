import socket

# Adres IP grupy multicast
MULTICAST_GROUP = '224.0.0.1'
# Numer portu
PORT = 5000

# Tworzenie gniazda
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ustawienie opcji gniazda dla multicastu
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

while True:
    message = input("Wpisz wiadomość: ")

    # Wysłanie komunikatu w trybie multicast
    sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))

    # Wysłanie komunikatu w trybie broadcast
    sock.sendto(message.encode(), ('<broadcast>', PORT))

# Zamknięcie gniazda
sock.close()
