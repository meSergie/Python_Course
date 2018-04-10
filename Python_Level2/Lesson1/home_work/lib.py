import json
import time

def main_loop_for_client(sock):

    message = \
    {
        'action': 'authenticate',
        'time': time.time()
    }

    message_json = message.dumps()
    message_buf = message_json.encode()

    sock.send(message_buf)