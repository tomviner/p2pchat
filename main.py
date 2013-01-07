import threading
import Queue

from server import serve
from client import relay
from ui import chat



def main():
    q = Queue.Queue()
    peers = set()
    threading.Thread(target=serve, args=(q, peers)).start()
    threading.Thread(target=requester, args=(q, peers)).start()
    threading.Thread(target=chat, args=(q, peers)).start()

