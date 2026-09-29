"""
##### Description
A simple program to demonstrate a printing queue using threads and semaphores in Python

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 28, 2026
"""

from src.job import Job
from src.printingqueue import PrintingQueue

def main():
	queue = PrintingQueue()

	jobs = []
	for i in range(1, 11):
		job = Job("Job " + str(i), queue)
		jobs.append(job)

	for job in jobs:
		job.start()

	for job in jobs:
		job.join()

	print("All printing jobs are finished")


if __name__ == "__main__":
	main()