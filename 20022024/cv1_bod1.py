#prvni ukol

import socket
#adresa a port prijemce (zada vyucujici)
host = "147.229.150.101" #upraveno na uciteluv
port = 50000

#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#zaslani zpravy
n = udp_socket.sendto(b"vecera", (host, port))
print("Odeslano {} byte\n".format(n))

#uzavreni socketu
udp_socket.close()