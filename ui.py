

def chat(q, peers, threads):
    while True:
        resp = ask("what is your message?")
        try:
            return raw_input(prompt)
        except KeyboardInterrupt:
            for thread in threads:
                thread.join()
            break


