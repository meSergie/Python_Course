
import socket
import lib
import time
import argparse
import sys

def run_server(port = 7777, addr = None):
    server_sock = socket.socket(
            family = socket.AF_INET,
            type = socket.SOCK_STREAM,
            proto = 0)

    server_sock.bind((addr, port)) #"127.0.0.1"
    server_sock.listen(5)

    while 1:
        sock, addr = server_sock.accept()
        # client_time = sock.recv(1024)
        # print(client_time.decode('ascii'))
        # timestr = str(time.time()) + "\n"
        # sock.send(timestr.encode('ascii'))
        lib.main_loop_for_server(sock)
        sock.close()

parser = argparse.ArgumentParser()
parser.add_argument('-p', type = int, nargs = 1)
parser.add_argument('-a', type = str, nargs = 1)
args = parser.parse_args()
print(args.a)

run_server(args.p[0], args.a[0])
