import sys
from stack import Stack

def infix_to_postfix(expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	op = Stack()
	postfix_list = []
	token_list = expr.split()

	for token in token_list:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_list.append(token)
		elif token == '(':
			op.push(token)
		elif token == ')':
			top_token = op.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = op.pop()
		else:
			while (not op.is_empty()) and \
				(prec[op.peek()] >= prec[token]):
				postfix_list.append(op.pop())
			op.push(token)

	while not op.is_empty():
		postfix_list.append(op.pop())
	return " ".join(postfix_list)

if __name__ == '__main__':
	expr = sys.argv[1]
	print(infix_to_postfix(expr))
		
