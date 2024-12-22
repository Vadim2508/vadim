import sys

def fibonacci(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <целое неотрицательное число>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    print(f"Fibonacci({n}) = {fibonacci(n)}")