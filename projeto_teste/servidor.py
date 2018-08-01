import socket
import struct
import random
import binascii

LED_TOGGLE_REQUEST = (0x79)
LED_SET_STATE = (0x7A)
LED_GET_STATE = (0x7B)
LED_STATE = (0x7C)

OP_REQUEST = (0x6E)
OP_RESULT = (0x6F)
OP_MULTIPLY = (0x22)
OP_DIVIDE = (0x23)
OP_SUM = (0x24)
OP_SUBTRACT = (0x25)

mathopreq = struct.Struct('I i I i f')
mathopreply = struct.Struct('I i I f I')

HOST = ''  # all interfaces
UDP_PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP IPv6
sock.bind((HOST, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print "received message: ", binascii.hexlify(data), " from: [", addr[0].strip(), " ]: ", addr[1]

    dados = struct.unpack_from(">B", data, 0)
    if dados[0] == LED_STATE:
        print "Recebeu LED_STATE"
        print dados[0]
        pass
    elif dados[0] == LED_GET_STATE:
        print "Recebeu LED_GET_STATE"
        pass
    elif dados[0] == LED_SET_STATE:
        print "Recebeu LED_SET_STATE"
        pass
    elif dados[0] == LED_TOGGLE_REQUEST:
        print "Recebeu LED_TOGGLE_REQUEST"

        RESPONSE = struct.pack('>BB', LED_SET_STATE, 0)

        print "UDP target IP: ", addr[0].strip()
        print "UDP target port: ", addr[1]
        print 'Packed Value   :', binascii.hexlify(RESPONSE)

        sock.sendto(RESPONSE, (addr[0].strip(), addr[1]))
        pass
    elif dados[0] == OP_REQUEST:
        print "Recebeu OP_REQUEST"
        request = struct.unpack_from('I i I i f', data, 0)
        if request[2] == OP_SUM:
            resultado = (request[1] + request[3]) * request[4]
        if request[2] == OP_SUBTRACT:
            resultado = (request[1] - request[3]) * request[4]
        if request[2] == OP_DIVIDE:
            resultado = (request[1] / request[3]) * request[4]
        if request[2] == OP_MULTIPLY:
            resultado = (request[1] * request[3]) * request[4]

        values = (OP_RESULT, resultado, resultado, resultado * 100000, mathopreply.size)
        RESPONSE = mathopreply.pack(*values)
        sock.sendto(RESPONSE, (addr[0].strip(), addr[1]))

        pass
    elif dados[0] == OP_RESULT:
        print "Recebeu OP_RESULT"
        pass