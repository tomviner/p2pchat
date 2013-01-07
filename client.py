import urllib2
import Queue


def relay(queue, peers):
	while True:
		try:
			message = queue.get(True, 2)  # Block for 2 seconds
		except Queue.Empty:
			pass
		else:
			print message

			for i in peers:
				if i != message['last_node']:
					url = "http://" + i + ":8000"
					data = message['msg']
					try:
						print urllib2.urlopen(url, data).read()
					except:
						set.remove(i)
