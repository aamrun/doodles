def fibo(n):
    if n<3:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

[print(str(i) + " , " + str(fibo(i))) for i in range(1,31)]