p2pchat
=======

A peer to peer chat network made of 3 parts:

    def chat(queue, peers, threads):
        """
        Accepts messages and adds them to the `queue`
        Optionally accepts an address too, which is added to `peers`
        """

    def serve(queue, peers, port=None):
        """
        Accept messages and add them to our `queue`,
        also add senders to our `peers` set
        """

    def relay(queue, peers, port):
        """
        Keep checking the `queue` for messages to send
        """