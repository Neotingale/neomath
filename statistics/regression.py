

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

