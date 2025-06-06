
def bisection(f : float, a : float, b : float, tol=1e-6, max_iter=100) -> float:
	for _ in range(max_iter):
		c = (a + b) / 2
		if abs(f(c)) < tol : return c
		if f(a) * f(c) < 0 : b = c
		else : a = c
	raise ValueError("No converge")


def false_position(f, a, b, tolerance=1e-6, iterations=50):
	for i in range(iterations):
		fa, fb = f(a), f(b)
		c = (a * fb - b * fa) / (fb - fa)
		fc = f(c)

		if abs(fc) < tolerance : return c

		if fa * fc < 0 : b = c
		else : a = c

	raise ValueError("Se llegó al límite de iteraciones")


def fixed_point(g, x0, tolerance=1e-6, iterations=50):
	for i in range(iterations):
		x1 = g(x0)
		error = abs(x1 - x0)
		if error < tolerance : return x1
		x0 = x1

	raise ValueError("Se llegó al límite de iteraciones")


def newton_raphson(f, f_prime, x0, tolerance=1e-6, iterations=50):
	for i in range(iterations):
		fx = f(x0)
		dfx = f_prime(x0)

		if dfx == 0 : raise ValueError("Derivada es cero, método no aplicable")

		x1 = x0 - fx / dfx
		error = abs(x1 - x0)
		if error < tolerance : return x1
		x0 = x1

	raise ValueError("Se llegó al límite de iteraciones")


def secant(f, x0, x1, tolerance=1e-6, iterations=50):
	for i in range(iterations):
		fx0, fx1 = f(x0), f(x1)
		if fx0 == fx1 : raise ValueError("División por cero")

		x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
		error = abs(x2 - x1)
		if error < tolerance : return x2
		x0, x1 = x1, x2

	raise ValueError("Se llegó al límite de iteraciones")


def jacobi(A, b, x0=None, tolerance=1e-6, iterations=100):
	n = len(A)
	x = [0.0 for _ in range(n)] if x0 is None else x0[:]

	for _ in range(iterations):
		x_new = x[:]
		for i in range(n):
			s = sum(A[i][j] * x[j] for j in range(n) if j != i)
			x_new[i] = (b[i] - s) / A[i][i]

		error = max(abs(x_new[i] - x[i]) for i in range(n))
		if error < tolerance : return x_new
		x = x_new

	raise ValueError("Se llegó al límite de iteraciones")


def gauss_seidel(A, b, x0=None, tolerance=1e-6, iterations=100):
	n = len(A)
	x = [0.0 for _ in range(n)] if x0 is None else x0[:]

	for _ in range(iterations):
		x_new = x[:]
		for i in range(n):
			s1 = sum(A[i][j] * x_new[j] for j in range(i))
			s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
			x_new[i] = (b[i] - s1 - s2) / A[i][i]

		error = max(abs(x_new[i] - x[i]) for i in range(n))
		if error < tolerance : return x_new
		x = x_new

	raise ValueError("Se llegó al límite de iteraciones")


def gauss_jordan(A: list[list[float]], b: list[float]) -> list[float]:
	"""

	"""
	n = len(b)
	M = [A[i][:] + [b[i]] for i in range(n)]

	for i in range(n):
		max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
		M[i], M[max_row] = M[max_row], M[i]

		pivot = M[i][i]
		if pivot == 0:
			raise ValueError("No unique solution exists")
		M[i] = [v / pivot for v in M[i]]

		for j in range(n):
			if j != i:
				factor = M[j][i]
				M[j] = [M[j][k] - factor * M[i][k] for k in range(n + 1)]

	return [M[i][-1] for i in range(n)]

