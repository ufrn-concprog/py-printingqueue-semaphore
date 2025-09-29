from job import Job
from printingqueue import PrintingQueue

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