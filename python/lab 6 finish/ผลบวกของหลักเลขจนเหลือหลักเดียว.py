num = int(input())
summ = 0
while True:
    if num > 0:
        a = num%10
        summ = summ + a
        num = num//10
        continue
    elif summ>= 10:
        b = summ%10
        c = summ//10
        summ = c+b
    else:
        break
print(summ)