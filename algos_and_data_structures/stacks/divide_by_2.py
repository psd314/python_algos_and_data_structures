from stack import Stack
import sys

def divide_by_2(n):
	remstack = Stack()
	
	while n > 0:
		rem = n % 2
		remstack.push(rem)
		n = n // 2

	bin_string = ""
	while not remstack.is_empty():
		bin_string = bin_string + str(remstack.pop())

	return bin_string

if __name__ == '__main__':
	n = int(sys.argv[1])
	print(divide_by_2(n))
