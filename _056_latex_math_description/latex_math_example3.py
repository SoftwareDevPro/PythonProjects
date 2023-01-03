
import latexify
import math
import sympy

@latexify.with_latex
def integral(x):
    return sympy.Integral(math.sin(x**2), x)

if __name__ == "__main__":
    print(integral)