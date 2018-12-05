def fibo(n):
    if n >= 2:
        f0 = 1
        f1 = 1
        i = 2
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
num = int(input())
oe = str(input())
if ((oe != 'O' and oe != 'o') and (oe != 'E' and oe !='e') ) or num < 0:
    ans = 'ERROR'
else:
    if (oe == 'O' or oe == 'o') and num == 0:
        ans = 'ERROR'
    elif (oe == 'O' or oe == 'o'):
        count = 0
        ans = 0
        while count <= num:
            if count % 2 == 1 :
                ans += fibo(count)
            count += 1
    else:
        count = 0
        ans = 0
        while count <= num:
            if count % 2 == 0:
                ans = ans + fibo(count)
            count += 1
print(ans)