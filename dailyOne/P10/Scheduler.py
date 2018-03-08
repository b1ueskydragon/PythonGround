import time
import threading


class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):  # この n なに?
        def call_after_sleep(n):
            time.sleep(n / 1000)
            f()

        t = threading.Thread(target=call_after_sleep)
        t.start()
