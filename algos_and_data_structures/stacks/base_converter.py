import sys
from stack import Stack

def base_converter(n, base):
	digits = "0123456789ABCDEF"
	s = Stack()

	while n > 0:
		rem = n % base
		s.push(rem)
		n = n // base

	new_string = ""
	while not s.is_empty():
		new_string = new_string + digits[s.pop()]

	return new_string

if __name__ == '__main__':
	n = int(sys.argv[1])
	base = int(sys.argv[2])
	print(base_converter(n, base))
