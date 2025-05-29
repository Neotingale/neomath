

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

def multiple_regression(x : list[float], y : list[float], degree : int = 2) -> list[float]:
	"""
	"""
	n = len(x)
	if n != len(y):
		raise ValueError("'x' y 'y' no tienen la misma longitud")

	X = [[sum(xi ** (i + j) for xi in x) for j in range(degree + 1)] for i in range(degree + 1)]

	F = [sum((x[i] ** j) * y[i] for i in range(n)) for j in range(degree + 1)]

	# X * A = F para hallar A
	def gauss_jordan(A : list[list[float]], b : list[float]) -> list[float]: # TODO Exportar a `numerics.solvers`
		size = len(b)
		for i in range(size) : A[i].append(b[i])

		for i in range(size):
			max_row = max(range(i, size), key=lambda r: abs(A[r][i]))
			A[i], A[max_row] = A[max_row], A[i]

			pivot = A[i][i]
			if pivot == 0 : raise ValueError("Sin solución única")
			A[i] = [x / pivot for x in A[i]]

			for j in range(size):
				if j != i:
					factor = A[j][i]
					A[j] = [A[j][k] - factor * A[i][k] for k in range(size + 1)]

		return [A[i][-1] for i in range(size)]

	A = gauss_jordan([row[:] for row in X], F[:])
	return A


