import sys
from stack import Stack

def par_checker(symbol_str):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_str) and balanced:
		symbol = symbol_str[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
		index += 1

	if balanced and s.is_empty():
		return True
	else:
		return False

if __name__ == '__main__':
	string = sys.argv[1]
	print(par_checker(string))
