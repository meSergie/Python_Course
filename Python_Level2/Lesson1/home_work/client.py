import socket
#import lib
import sys

addr = sys.argv[1]
port = int(sys.argv[2])
print(str(addr), port)
sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM,
        proto = 0)

sock.connect((addr, port))
#lib.main_loop_for_client(sock)
messege = sock.recv(1024)
print(messege.decode('ascii'))
sock.close()
