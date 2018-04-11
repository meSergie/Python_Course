import unittest
from unittest.mock import Mock
import json
import lib
import time

class STest(unittest.TestCase):

    def test_server(self):

        to_client = \
        {
            'action': 'probe',
            'time': time.time()
        }
        from_client = \
        {
        'action': 'presence',
        'time': time.time(),
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
            }
        }

        to_client_buf = json.dumps(to_client).encode()
        from_client_buf = json.dumps(from_client).encode()

        virt_sock = Mock()
        virt_sock.send.return_value = to_client_buf
        virt_sock.recv.return_value = from_client_buf
        
        res = from_client['action'], to_client['action']
        really_result = lib.main_loop_for_server(virt_sock)
        #print(res, really_result)
        self.assertEqual(res, really_result)

if __name__ == '__main__':
    unittest.main()