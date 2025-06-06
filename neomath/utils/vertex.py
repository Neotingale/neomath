
def parabola_vertex(a1 : float, a2 : float) -> float:
	if a2 == 0 : raise ValueError("No es una parábola válida si a2 = 0")
	return -a1 / (2 * a2)
