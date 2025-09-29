from threading import Thread, current_thread
from printingqueue import PrintingQueue

class Job(Thread):
    def __init__(self, id, queue):
        super().__init__()
        self.name = id
        self.queue = queue

    def run(self):
        print("Sending printing job to printer:", current_thread().name)
        self.queue.printJob()