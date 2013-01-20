import sys
import urllib2
import urlparse

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


def get_ChatHandler(_queue, _peers):
    """
    Use a closure to insert our queue and peers into the server class
    """
    class ChatHandler(BaseHTTPRequestHandler):
        queue = _queue
        peers = _peers

        def process_msg(self, msg, their_port):
            print 'SV:', self.queue, self.peers
            their_port = their_port or 8000
            their_url = '%s:%s' % (self.client_address[0], their_port)
            print 'SV:', their_url
            self.peers.add(their_url)
            message = {
                'msg': msg,
                'last_node': their_url,
            }
            print 'SV:', 'message:', msg
            self.queue.put(message)

        def do_GET(self):
            qs = self.path.partition('?')[2]
            print '\nSV:', 'qs', repr(urllib2.unquote(qs))
            dic = urlparse.parse_qs(qs)
            msg = ','.join(dic.get('msg', ['<no msg>']))
            their_port = ''.join(dic.get('my_port', []))

            self.process_msg(msg, their_port)
            self.send_response(200, "<html><body>This is the index page</body></html>")

        def do_POST(self):
            content_len = int(self.headers.getheader('content-length'))
            post_body = self.rfile.read(content_len)
            print '\nSV:', post_body
            self.process_msg(post_body)
            self.send_response(200, "OK")
    return ChatHandler


def serve(queue, peers, port=None):
    """
    Accept messages and add them to our `queue`,
    also add senders to our `peers` set
    """
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, get_ChatHandler(queue, peers))
    sa = httpd.socket.getsockname()
    print 'SV:', "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    serve(None, None, int(sys.argv[1]))

