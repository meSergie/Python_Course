import json
import time

def main_loop_for_client(sock):

    messege = \
    {
        'action': 'authenticate',
        'time': time.time()
    }

    messege_json = messege.dumps()
    messege_buf = messege_json.encode()

    sock.send(messege_buf)