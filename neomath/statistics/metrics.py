
def r_squared(y_true : list[float], y_pred : list[float]) -> float:
	"""
	"""
	mean_y = sum(y_true) / len(y_true)
	ss_tot = sum((yi - mean_y) ** 2 for yi in y_true)
	ss_res = sum((yi - ypi) ** 2 for yi, ypi in zip(y_true, y_pred))
	return 1 - ss_res / ss_tot