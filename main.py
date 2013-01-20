import sys
import threading
import Queue

from server import serve
from client import relay
from ui import chat


def main():
    """
    Accept and send messages in a peer to peer chat network.
    """
    listening_port = 8000
    if sys.argv[1:]:
        listening_port = int(sys.argv[1])

    q = Queue.Queue()
    peers = set()
    server = threading.Thread(
        target=serve,
        name=serve.func_name,
        args=(q, peers),
        kwargs={'port': listening_port}
    )
    relayer = threading.Thread(
        target=relay,
        name=relay.func_name,
        args=(q, peers),
        kwargs={'port': listening_port}
    )
    threading.Thread(
        target=chat,
        name=chat.func_name,
        args=(q, peers),
        # send the first two threads so they can be stopped
        kwargs={'threads':(server, relayer)}
    ).start()
    server.start()
    relayer.start()

if __name__ == '__main__':
    main()
