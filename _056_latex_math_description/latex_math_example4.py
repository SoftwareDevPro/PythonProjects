
import latexify
from sympy import *

@latexify.with_latex
def derivative(x):
    m, n, a, b = symbols('m n a b')
    expr = (a*x + b)**m
    return expr.diff((x, n))

if __name__ == "__main__":
    print(derivative)