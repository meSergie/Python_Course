
import unittest
from unittest.mock import Mock
import json
import lib
import time

class CTest(unittest.TestCase):

    def test_client(self):

        from_serv = \
        {
            'action': 'probe',
            'time': time.time()
        }
        to_serv = \
        {
        'action': 'presence',
        'time': time.time(),
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
            }
        }

        from_serv_buf = json.dumps(from_serv).encode()
        to_serv_buf = json.dumps(to_serv).encode()

        virt_sock = Mock()
        virt_sock.recv.return_value = from_serv_buf
        virt_sock.send.return_value = to_serv_buf

        res = from_serv['action'], to_serv['action']
        really_result = lib.main_loop_for_client(virt_sock)
        #print(res, really_result)
        self.assertEqual(res, really_result)

if __name__ == '__main__':
    unittest.main()