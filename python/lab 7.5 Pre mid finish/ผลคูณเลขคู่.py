num = int(input())
a = 1
while num > 0:
    ans = num % 10
    if ans%2 == 1:
        pass
    elif ans%2 == 0:
        a = a*ans
    num = num // 10
if a == 1:  
    print('-1')
else:
    print(a)