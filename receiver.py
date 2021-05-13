import socket
import numpy as np  

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
transmissor = ("127.0.0.1", 2020)
receptor = ("127.0.0.1", 3030)
socketUDP.bind(receptor)
buff_size = 10000
sequence = 0



def rdt_rcv():
    while True:
        message, source = socketUDP.recvfrom(buff_size)
        if source == transmissor:
            print("Pacote recebido, checando se é corrupto...")
            if source.is_not_corrupt(source):
                print("não é corrupto")
                sequence, source = sequence.extract(message)
                if sequence == sequence:
                    print("Numero de sequencia esperado, Reenviando pacotes..", sequence)
                    sequence ^= +1
                    return np.frombuffer(message, dtype=np.uint16)
                else:
                    print("Pacote duplicado")
                    socketUDP.sendto(transmissor(b"ACK"),transmissor)
            else:
                print("Pacote corrupto")
                socketUDP.sendto(transmissor(b"NAK"), transmissor)

        
                

if __name__ == "__main__":
    rcvpkt = rdt_rcv()
    while True:
     rcvpkt.rdt_rcv()
     print(f"Dados recebidos {rcvpkt}")
