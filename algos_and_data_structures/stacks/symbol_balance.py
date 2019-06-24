import sys
from stack import Stack

def balance_check(string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(string) and balanced:
		symbol = string[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1
	
	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(open_, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open_) == closers.index(close)

if __name__ == '__main__':
	string = sys.argv[1]
	print(balance_check(string))
