# import SimpleHTTPServer

# class ChatServer(SimpleHTTPServer):
# 	do_get():
# 		print 'hello from file'
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class ChatHandler(BaseHTTPRequestHandler):

	
	def do_GET(self):
		self.send_response(200,"<html><body>This is the index page</body></html>")

	def do_POST(self):
		content_len = int(self.headers.getheader('content-length'))
		post_body = self.rfile.read(content_len)
		print post_body
		self.send_response(200,"OK")


def serve(queue, peers):
	HandlerClass = ChatHandler
	Protocol     = "HTTP/1.0"

	if sys.argv[1:]:
	    port = int(sys.argv[1])
	else:
	    port = 8000
	server_address = ('0.0.0.0', port)

	HandlerClass.protocol_version = Protocol
	httpd = HTTPServer(server_address, HandlerClass)

	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "..."
	httpd.serve_forever()

if __name__ == '__main__':
	serve(None, None)

