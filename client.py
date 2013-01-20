import urllib
import urllib2
import Queue


def relay(queue, peers, port):
    """
    Keep checking the `queue` for messages to send
    """
    while True:
        try:
            message = queue.get(True, 2)  # Block for 2 seconds
        except Queue.Empty:
            pass
        else:
            print '\nCL:', message
            print peers
            last_node = message['last_node']
            qs = urllib.urlencode({
                'msg': message['msg'],
                'my_port': port,
            })

            if not peers:
                print 'CL:', 'no peers to contact'
            elif peers == set([last_node]):
                print 'CL:', 'only peer is sender'


            for peer_url in peers.copy():
                if peer_url != last_node:
                    url = "http://%s/?%s" % (peer_url, qs)
                    print 'CL:', 'GET', url
                    try:
                        print 'CL:', urllib2.urlopen(url).read()
                    except urllib2.URLError, e:
                        print 'CL:', repr(e)
                        print 'CL:', 'removing', peer_url
                        peers.remove(peer_url)
