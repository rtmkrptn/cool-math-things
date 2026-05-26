import numpy as np

FUNCTIONS = {
		'square': lambda x: x**2,
		'sin': lambda x: np.sin(x),
		'exp': lambda x: np.exp(x),
		'log': lambda x: np.log(x)
	}

def function_eval(functions: list[str],x: float):
    iteration = x
    for func in reversed(functions):
        iteration = FUNCTIONS[func](iteration)
    return iteration

def compute_chain_rule_gradient(functions: list[str], x: float, h=1e-7) -> float:
    return (function_eval(functions,x+h)-function_eval(functions,x-h))/(2*h)