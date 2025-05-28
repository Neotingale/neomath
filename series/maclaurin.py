
def maclaurin(f_derivatives : list[float], x : float, terms : int) -> float:
	return sum((f_derivatives[n] * x ** n) / factorial(n) for n in range(terms))
