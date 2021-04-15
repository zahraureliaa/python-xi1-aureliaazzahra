def deret_fibo(n):
    if n <= 1:
        return n
    else:
        return(deret_fibo(n-2) + deret_fibo(n-1))
print(deret_fibo(5))