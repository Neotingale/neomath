from algebra import matrix
from constants import math_constants, physics_constants
from core import expr, symbols, functions
from numerics import evaluate_polynomial, bisection, secant, gauss_seidel, gauss_jordan, false_position, newton_raphson, jacobi, fixed_point
from series import maclaurin
from statistics import linear_regression, polynomial_regression, r_squared
from utils import parabola_vertex

__all__ = [
	'matrix',

	'math_constants', 'physics_constants',

	'expr', 'symbols', 'functions',

	'evaluate_polynomial', 'bisection', 'secant', 'gauss_seidel', 'gauss_jordan',
	'false_position', 'newton_raphson', 'jacobi', 'fixed_point',

	'maclaurin',

	'linear_regression', 'polynomial_regression', 'r_squared',

	'parabola_vertex'
]
