import urllib2


def relay(queue, peers):
	message = queue.get(True, 2)  # Block for 2 seconds
	for i in peers:
		if i != message['last_node']:
			url = i
			data = message['msg']
			print urllib2.urlopen(url, data).read()
