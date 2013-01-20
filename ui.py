import re


def chat(queue, peers, threads):
    """
    Accepts messages and adds them to the `queue`
    Optionally accepts an address too, which is added to `peers`
    """
    print 'UI:', 'starting chat ui'
    while True:
        try:
            print '\nUI:', 'you are connected to', peers
            resp = raw_input("UI: Enter (new recipient IP:PORT) and message?\n")

            if 'quit' in resp.lower():
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            print 'UI:', 'QUIT'
            for thread in threads:
                print 'UI:', 'attempt to kill', thread
                # I'm sure this is bad, but it does work!
                thread._Thread__stop()
            break
        else:
            ip_re = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            port_re = ':\d{4}'
            addr = re.findall(r'((?:%s)?)(%s)(?=\s*)' % (ip_re, port_re), resp)
            if addr:
                ip, port = addr[0]
                peers.add(ip+port)
        print 'UI:', repr(resp)
        message = {
            'msg': resp,
            'last_node': None,
        }
        queue.put(message)



