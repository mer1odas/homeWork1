def dele(n):
    fib = 1
    fib_p =0 
    sum1 = 1
    for i in range(n - 2):
        fib_p1 = fib
        print(fib, "-------", fib_p)
        fib = fib + fib_p
        print(fib)
        fib_p = fib_p1
        sum1 += fib 
    return sum1 

print(dele(5))