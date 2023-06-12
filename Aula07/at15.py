a = 0
b= 1
for i in range(1, 11):
    fib = a + b
    a, b = b, fib
    print(fib)
