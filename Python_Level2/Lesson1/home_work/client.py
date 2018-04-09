import socket
#import lib
import sys
import time

addr = sys.argv[1]
port = int(sys.argv[2])
print(str(addr), port)
sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM,
        proto = 0)

sock.connect((addr, port))
timestr = str(time.time()) + "\n"
out_time = sock.send(timestr.encode('ascii'))
#lib.main_loop_for_client(sock)
messege = sock.recv(1024)
print(messege.decode('ascii'))
server_time = float(messege.decode('ascii'))
recv_time = time.time() - server_time
print('time to recieve =', recv_time)
sock.close()
