import urllib2
import Queue


def relay(queue, peers):
	while True:
		try:
			message = queue.get(True, 2)  # Block for 2 seconds
		except Queue.Empty:
			pass
		else:
			for i in peers:
				if i != message['last_node']:
					url = "http://" + i + ":8000"
					data = message['msg']
					print urllib2.urlopen(url, data).read()
