
import latexify
import math

@latexify.with_latex
def sinx(x):
    if x == 0:
        return 1
    else:
        return math.sin(x) / x()

if __name__ == "__main__":
    print(sinx)