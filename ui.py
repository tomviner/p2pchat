

def chat(queue, peers, threads):
    print 'starting chat ui'
    while True:
        try:
            print 'you are connected to', peers
            resp = raw_input("what is your message? ")
        except KeyboardInterrupt:
            print 'QUIT'
            for thread in threads:
                print 'attempt to kill', thread
                thread.join()
            break
        message = {
            'msg': resp,
            'last_node': None,
        }
        queue.put(message)



