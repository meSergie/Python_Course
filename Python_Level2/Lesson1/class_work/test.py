
import unittest
import json
from unittest.mock import Mock
import lib

class CTest(unittest.TestCase):

    def test_1(self):

        x = 10
        y = 5
        res = lib.div(x, y)

        self.assertEqual(res, 10 / 5)

    def test_2(self):

        x = 8
        y = 0

        self.assertRaises(AssertionError, lib.div, x, y)

    def test_3(self):

        res = \
        {
            "+" : 20,
            "-" : 10
        }
        res_buf = json.dumps(res).encode()

        virt_sock = Mock()
        virt_sock.send.return_value = None
        virt_sock.recv.return_value = res_buf
        # __call__

        really_result = lib.main_loop_for_server(virt_sock)

        self.assertEqual(res["+"], really_result["+"])
        self.assertEqual(res["-"], really_result["-"])

