
import sys

def Fibonacci(N):
    # Base case
    num_1 = 0
    num_2 = 1

    print(num_1, num_2, end=" ")

    N -= 2
    
    while N > 0:
        print(num_1 + num_2, end=" ")

        temp = num_2
        num_2 = num_1 + num_2
        num_1 = temp

        N -= 1

if __name__ == "__main__":
    N = 5
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    Fibonacci(N)
