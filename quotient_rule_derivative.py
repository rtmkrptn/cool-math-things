import numpy as np
from numpy.polynomial import polynomial as poly

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    # Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    g_coeffs.reverse()
    h_coeffs.reverse()

    g = poly.Polynomial(g_coeffs)
    h = poly.Polynomial(h_coeffs)

    g_dash = g.deriv()
    h_dash = h.deriv()

    return (h(x)*g_dash(x)-h_dash(x)*g(x))/h(x)**2

print(round(quotient_rule_derivative([1, 0, 1], [1, 2], 2.0), 4))
