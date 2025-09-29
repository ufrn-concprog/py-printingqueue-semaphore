from threading import Semaphore, current_thread
from time import sleep
from random import randint

class PrintingQueue:
    def __init__(self):
        self.semaphore = Semaphore()

    def printJob(self):
        self.semaphore.acquire()
        try:
            time = randint(1, 5)
            print(current_thread().name, "printing for", time, "second(s)")
            sleep(time)
        finally:
            self.semaphore.release()
    