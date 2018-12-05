num = int(input())
a = 0
while num > 0:
    ans = num % 10
    if ans%2 == 0:
        pass
    elif ans%2 == 1:
        a = a+ans
    num = num // 10
if a == 0:  
    print('-1')
else:
    print(a)