import json
import time

def main_loop_for_client(sock):

    message = \
    {
        'action': 'presence',
        'time': time.time(),
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
            }

    }

    message_json = json.dumps(message)
    message_buf = message_json.encode()

    resp = sock.recv(1024).decode()
    resp_json = json.loads(resp)
    print(resp_json)
    if resp_json['action'] == 'probe':
        sock.send(message_buf)
    
def main_loop_for_server(sock):

    message = \
    {
        'action': 'probe',
        'time': time.time()
    }

    message_json = json.dumps(message)
    message_buf = message_json.encode()
    sock.send(message_buf)
    
    resp = sock.recv(1024)
    resp_json = json.loads(resp)
    print(resp_json)
    if resp_json['action'] == 'presence':
        message =\
        {
            "response": 200,
            "time": time.time(),
            "alert": "OK"
        }
        message_json = json.dumps(message)
        message_buf = message_json.encode()
        sock.send(message_buf)