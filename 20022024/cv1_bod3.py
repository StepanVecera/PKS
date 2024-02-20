#TRETI UKOL
import socket
import struct
import time
#adresa a port prijemce (zada vyucujici)
host = "147.229.150.101" #upraveno na uciteluv
port = 50000

id = 230345
pc = 80
seq =0
file = "udp.log"

#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", port))

#seq, id a pc jsou prenasena cisla
for i in range(5):
#seq, id a pc jsou prenasena cisla
    seq = i
    data = struct.pack("!LLL", seq, id, pc)

#zaslani zpravy
    n = udp_socket.sendto(data, (host, port))
    print("Odeslano {} byte\n".format(n))
    time.sleep(0.5)
#----------------------------------------------------------------------------
    try:
        data, address = udp_socket.recvfrom(512)
        Rseq, Rn1, Rn2 = struct.unpack("!LLL", data)
    except TimeoutError:
        print("No response from server")
    except struct.error:
        print("Unable to unpack packet from {}".format(address))
    else:
        #vypis prijatych dat
        log = "Received: a={}, p={}, s={}, n1={}, n2 ={}".format(*address, Rseq, Rn1, Rn2)
        print(log)
        fo = open(file, "a") #soubor otevřít v řežimu “append”
        fo.write(log + "\n") #přidat znak nového řádku
        fo.close

        time.sleep(0.5)

#uzavreni socketu
udp_socket.close()