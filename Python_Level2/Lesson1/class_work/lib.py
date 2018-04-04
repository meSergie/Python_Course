
import json

def main_loop_for_server(sock):

    evl = \
    {
        "+" : (10, 30),
        "-" : (40, 20),
        "*" : (5, 7),
        "/" : (9, 2)
    }
    evl_json = json.dumps(evl)
    buf = evl_json.encode()

    sock.send(buf)
    result_buf = sock.recv(1024)
    
    result = json.loads(result_buf.decode())

    print(result)

    return result

def main_loop_for_client(sock):

    buf = sock.recv(1024)
    evl = json.loads(buf.decode())

    func = \
    {
        "+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y,
        "*" : lambda x, y: x * y,
        "/" : div
    }

    result = {}

    for i in evl:

        result[i] = func[i](evl[i][0], evl[i][1])

    result_json = json.dumps(result)
    result_buf = result_json.encode()
    sock.send(result_buf)

#############################################################################

def div(x, y):
    """

    >>> div(20, 10)
    2.0

    """

    # assert isinstance(x, float), "X - не вещественное"
    assert y != 0, "Y равен 0"

    return x / y

