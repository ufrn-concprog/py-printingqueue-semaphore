"""
##### Description
A printing queue as a shared resource

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 28, 2026
"""

from threading import Semaphore, current_thread
from time import sleep
from random import randint

class PrintingQueue:
    """A queue that allows only one thread to print at a time.

    Each call to :meth:`printJob` acquires the queue's semaphore, simulates
    printing for a random duration, and releases the semaphore afterward.
    """

    def __init__(self):
        """Create a queue with a semaphore permitting one active printing job."""
        self.semaphore = Semaphore()

    def printJob(self):
        """Simulate printing while holding exclusive access to the printer.

        The simulated print duration is a random integer from one to five
        seconds. Other printing jobs (threads) block until the current job releases 
        the semaphore.
        """
        self.semaphore.acquire()
        try:
            time = randint(1, 5)
            print(current_thread().name, "printing for", time, "second(s)")
            sleep(time)
        finally:
            self.semaphore.release()
    