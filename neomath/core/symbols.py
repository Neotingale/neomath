from expr import Add, Mul, Pow

class Symbol:
	def __init__(self, name : str):
		self.name = name

	def __repr__(self):
		return self.name

	def __add__(self, other):
		return Add(self, other)

	def __radd__(self, other):
		return Add(other, self)

	def __mul__(self, other):
		return Mul(self, other)

	def __rmul__(self, other):
		return Mul(other, self)

	def __pow__(self, power):
		return Pow(self, power)
