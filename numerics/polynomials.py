
def evaluate_polynomial(coeffs: list[float], x: float) -> float:
	return sum(a * (x ** i) for i, a in enumerate(coeffs))
