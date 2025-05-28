def r_squared(y_true : list[float], y_pred : list[float]) -> float:
	mean_y = sum(y_true) / len(y_true)
	ss_tot = sum((yi - mean_y) ** 2 for yi in y_true)
	ss_res = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true)))
	return 1 - (ss_res / ss_tot)