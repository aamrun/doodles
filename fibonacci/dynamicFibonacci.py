fiboList = [1,1]

def fibo(n):
    length = len(fiboList)

    if n<=length:
        return fiboList[n-1]
    else:
        fiboList.append(fiboList[-2] + fiboList[-1])
        return fiboList[-1]

[print(str(i) + " , " + str(fibo(i))) for i in range(1,31)]