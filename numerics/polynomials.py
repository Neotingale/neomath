
def evaluate_polynomial(x : float, coefs : list[float]) -> float:
	return sum(coefs[i] * x**i for i in range(len(coefs)))
