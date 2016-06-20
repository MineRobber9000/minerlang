#!/usr/bin/python
# ml.py - the interpreter for the language

class minerlang:
	VarWords = {
		"+": lambda self: self.stack.pop()+self.stack.pop(),
		"-": lambda self: self.subtract(),
		"*": lambda self: self.stack.pop()*self.stack.pop(),
		"/": lambda self: self.divide(),
		"store": lambda self: self.store(),
		"load": lambda self: self.load(),
		"tell": lambda self: self.stack[len(self.stack)-1],
		"tellstack": lambda self: "["+(", ".join([str(x) for x in self.stack]))+"]"
	}
	"""A minerlang interpreter."""
	def __init__(self):
		self.stack = []

	def run(self, macro):
		macro_parts = macro.split(" ");
		for part in macro_parts:
			if part in ("+","-","*","/","tell","clear","store","load","tellstack"):
				if part == "tell" or part == "tellstack":
					print(self.VarWords[part](self))
				elif part == "clear":
					self.stack = []
				elif part == "store" or part == "load":
					self.VarWords[part](self)
				else:
					stack = self.stack[:]
					for n in [1,2]:
						idgaf = stack.pop()
					stack.append(self.VarWords[part](self))
					self.stack = stack;
			else:
				self.stack.append(int(part))

	def clearStack(self):
		self.run("clear")

	def subtract(self):
		two = self.stack.pop()
		one = self.stack.pop()
		return one - two

	def divide(self):
		two = self.stack.pop()
		one = self.stack.pop()
		return one / two

	def store(self):
		self.register = self.stack
		self.stack = []

	def load(self):
		self.stack = self.register
		self.register = []
