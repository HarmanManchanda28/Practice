def factorial (n):
    if n == 1:
        return 1
    else:
        return factorial (n-1) * n

print (factorial(5))


def factorial_loop (n):
    factorial = 1
    for i in range(n):
        factorial = factorial * (i+1)
    return factorial

print (factorial_loop(5))