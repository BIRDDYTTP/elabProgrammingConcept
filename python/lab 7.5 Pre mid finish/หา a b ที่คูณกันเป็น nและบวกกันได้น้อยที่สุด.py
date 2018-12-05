num = int(input())
x = 1
ans1 = num+1
while x <= num:
    y = 1
    while y <= num:
        if x*y == num:
            ans = x+y
            if ans< ans1:
                ans1 = ans
                y += 1
            else:
                y += 1
        else:
            y += 1
    x += 1
print("%d"%ans1)