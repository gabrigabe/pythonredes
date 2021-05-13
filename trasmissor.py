import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
transmissor = ("localhost", 2020)
receptor = ("localhost", 3030)
buff_size = 1024
socket.bind(transmissor)

def calculate_checksum(data):
    data_sum = 0
    for element in data:
        data_sum +=element
    return ~data_sum

def verify_checksum(checksum, data):
   data_sum = 0
    for element in data:
      data_sum +=element
    return ~data_sum


def udt_send(packet):
    socketUDP.sendto(packet, receptor)   

def rdt_rcv():
     while True:
        message, source = socket.recvfrom(buff_size)
        if source == receptor:
            return message

def rdt_send(data):
    packet = []
    packet.append(0)
    packet.append(calculate_checksum(data   ))
    packet.extend(data)

    udt_send(packet)

    rcvpkt = rdt_rcv()
    checksum = rcvpkt[1]
    if verify_checksum(checksum, data)