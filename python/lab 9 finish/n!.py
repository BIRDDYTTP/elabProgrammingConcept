def fac(n):
    if n == 0:
        return 1
    else:
        count = 1
        ans = 1
        while count <= n:
            ans *= count
            count += 1
        return ans
    
n = int(input("Enter n: "))    
print("%d!"%(n), "=",fac(n))