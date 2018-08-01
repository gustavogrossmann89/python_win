import socket
import struct
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

# IPV6 - Bourder Router
# UDP_PORT = 8802
# UDP_IP = "2804:7f4:3b80:9440:5748:f6e0:f733:4c6b"

# CLIENTE PRATICA SNIFFER COM PORTA ERRADA
#UDP_PORT = 8802
#UDP_IP = "fe80::212:4b00:f28:c303"

# IPV4 LOCAL
UDP_PORT = 3000
UDP_IP = "127.0.0.1"

#MESSAGE = struct.pack('>BB',LED_STATE,1)
#MESSAGE = struct.pack('>B', LED_TOGGLE_REQUEST)

values = (OP_REQUEST, 5, OP_MULTIPLY, 4, 1)
MESSAGE = mathopreq.pack(*values)

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print 'Packed Value   :', binascii.hexlify(MESSAGE)

# socket.SOCK_DGRAM = UDP connection
# PACOTES IPV4
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# PACOTES IPV6
#sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

sock.bind((HOST, 3001))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes

    unpacked_data = struct.unpack_from(">BB", data, 0)
    print "received message: ", unpacked_data, " from: [", addr[0].strip(), " ]: ", addr[1]

    unpacked_data = struct.unpack_from(">BB", data, 0)
    op = unpacked_data[0]
    if op == LED_STATE:
        print "Recebeu LED_STATE"
        print unpacked_data[1]
        pass
    elif op == LED_GET_STATE:
        print "Recebeu LED_GET_STATE"
        pass
    elif op == LED_SET_STATE:
        print "Recebeu LED_SET_STATE"
        estado = unpacked_data[1]
        print "Estado:", estado
        RESPONSE = struct.pack('>BB', LED_STATE, estado)

        print "UDP target IP: ", addr[0].strip()
        print "UDP target port: ", addr[1]
        print 'Packed Value   :', binascii.hexlify(RESPONSE)

        sock.sendto(RESPONSE, (addr[0].strip(), addr[1]))
        pass
    elif op == LED_TOGGLE_REQUEST:
        print "Recebeu LED_TOGGLE_REQUEST"
        pass
    elif op == OP_REQUEST:
        print "Recebeu OP_REQUEST"
        pass
    elif op == OP_RESULT:
        print "Recebeu OP_RESULT"
        result = struct.unpack_from('I i I f I', data, 0)
        print result[0]
        print result[1]
        print result[2]
        print result[3]
        print result[4]

        pass