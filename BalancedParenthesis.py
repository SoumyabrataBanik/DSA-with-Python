"""
Use a stack to check if the given string has balanced parentheses or not.

For example:
    (), ()(), (({[]})) <- Balanced
    ((), {{{}]), [][]]] <- Not Balanced

Balanced Example: {[]}
Non-balanced Example: (((), ))

"""

from Stack import Stack

"""
class Stack:

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		return

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		return

	def is_empty(self):
		return self.items == []
"""

def is_balanced_parentheses(parent_string):

	stack = Stack()
	index = 0
	is_balanced = True
	opening_parentheses = ["(", "{", "["]

	while index < len(parent_string) and is_balanced:
		if parent_string[index] in opening_parentheses:
			stack.push(parent_string[index])
		else:
			if stack.is_empty():
				is_balanced = False
			else:
				top = stack.pop()
				if not ismatch(top, parent_string[index]):
					is_balanced = False
		index += 1

	return stack.is_empty() and is_balanced

"""
	if stack.is_empty and is_balanced:
		return True
	else:
		return False
"""


def ismatch(p1, p2):

	if p1 == "(" and p2 == ")":
		return True
	elif p1 == "{" and p2 == "}":
		return True
	elif p1 == "{" and p2 == "}":
		return True
	else:
		return False


def main():

	parent_string = input("Enter the string: ")
	isbalanced = is_balanced_parentheses(parent_string)
	print(isbalanced)


if __name__ == "__main__":
	main()

