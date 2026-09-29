"""
##### Description
A thread as a printing job sent to shared printing queue

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 28, 2026
"""

from threading import Thread, current_thread
from src.printingqueue import PrintingQueue

class Job(Thread):
    """Represents a print job that can be executed in a separate thread."""

    def __init__(self, id, queue):
        """Initialize a named printing-job thread.

        :param id: The ID of the print job
        :param queue: A reference to the PrintingQueue to which the job belongs
        """
        super().__init__()
        self.name = id
        self.queue = queue

    def run(self):
        """Submit this job to the printing queue."""
        print("Sending printing job to printer:", current_thread().name)
        self.queue.printJob()