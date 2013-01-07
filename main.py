import threading
import Queue

from server import serve
from client import relay
from ui import chat



def main():
    q = Queue.Queue()
    peers = set()
    s = threading.Thread(target=serve, args=(q, peers)).start()
    r = threading.Thread(target=requester, args=(q, peers)).start()
    threading.Thread(target=chat, args=(q, peers), kwargs={threads=(s, r)}.start()

