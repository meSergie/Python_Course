#!/usr/bin/env python3

import socket
import lib

sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM,
        proto = 0)

sock.connect(("127.0.0.1", 7777))
lib.main_loop_for_client(sock)
sock.close()

