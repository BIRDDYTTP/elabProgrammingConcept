def fibo(n):
    if n >= 3:
        f0 = 1
        f1 = 1
        i = 3
        while i <= n:
            f2 = f1+f0
            f0 = f1
            f1 = f2
            i +=1
        return f2
    elif n == 0:
        return 1
    else:
        return 1
    
n = int(input("Enter n: "))    
print("fibo(%d) = %d"% (n,fibo(n)))