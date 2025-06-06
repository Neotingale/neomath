from numerics.solvers import gauss_jordan


def linear_regression(x : list[float], y : list[float]) -> tuple[float, float]:
	"""
	"""
	n = len(x)
	sum_x = sum(x)
	sum_y = sum(y)
	sum_xx = sum(xi**2 for xi in x)
	sum_xy = sum(x[i] * y[i] for i in range(n))

	b = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
	a = (sum_y - b * sum_x) / n
	return a, b


def polynomial_regression(x : list[float], y : list[float], degree : int = 2) -> list[float]:
	"""
	"""
	if len(x) != len(y) : raise ValueError("'x' y 'y' deben tener el mismo tamaño")

	n = len(x)
	X = [[sum(xi ** (i + j) for xi in x) for j in range(degree + 1)] for i in range(degree + 1)]
	F = [sum((x[i] ** j) * y[i] for i in range(n)) for j in range(degree + 1)]

	return gauss_jordan(X, F)



