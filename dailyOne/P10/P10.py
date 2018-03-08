"""
Calls f after n milliseconds
:param f: function
:param n: milliseconds
"""

import time


def job_scheduler(f, n):
    time.sleep(n / 1000)
    f()
