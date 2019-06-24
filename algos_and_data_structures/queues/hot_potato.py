import sys
from queue import Queue

def hot_potato(namelist, num):
	sim_queue = Queue()

	for name in namelist:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()

	return sim_queue.dequeue()

if __name__ == '__main__':
	print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
