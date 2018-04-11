import socket
import lib
import sys
import time

addr = sys.argv[1]
port = int(sys.argv[2])
# print(str(addr), port)
sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM,
        proto = 0)

sock.connect((addr, port))

# timestr = str(time.time()) + "\n"
# out_time = sock.send(timestr.encode('ascii'))
# lib.main_loop_for_client(sock)
# message = sock.recv(1024)
# print(message.decode('ascii'))
# server_time = float(message.decode('ascii'))
# recv_time = time.time() - server_time
# print('time to recieve =', recv_time)
lib.main_loop_for_client(sock)
sock.close()
