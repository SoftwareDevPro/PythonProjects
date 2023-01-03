
import latexify
import math

@latexify.with_latex
def solve(x, y, z):
    return (-y + math.sqrt(y ** 3 - 6*x*z)) / (3*(x+y))

if __name__ == "__main__":
    print(solve)




