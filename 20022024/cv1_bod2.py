#prvni ukol

import socket
import struct
import time
#adresa a port prijemce (zada vyucujici)
host = "147.229.150.101" #upraveno na uciteluv
port = 50000

id = 230345
pc = 80
seq =0

#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
#seq, id a pc jsou prenasena cisla
    seq = i
    data = struct.pack("!LLL", seq, id, pc)

#zaslani zpravy
    n = udp_socket.sendto(data, (host, port))
    print("Odeslano {} byte\n".format(n))
    time.sleep(0.5)

#uzavreni socketu
udp_socket.close()