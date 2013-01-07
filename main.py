import threading
import Queue

from server import serve
from client import relay
from ui import chat

def main():
    q = Queue.Queue()
    peers = set()
    print 1
    s = threading.Thread(target=serve, args=(q, peers)).start()
    print 2
    r = threading.Thread(target=relay, args=(q, peers)).start()
    print 3
    threading.Thread(target=chat, args=(q, peers), kwargs={'threads':(s, r)}).start()
    print 4

if __name__ == '__main__':
    main()
