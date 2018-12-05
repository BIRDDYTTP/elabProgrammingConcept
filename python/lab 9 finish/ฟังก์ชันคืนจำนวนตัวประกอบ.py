def factor_count(n):
    count = 1
    count2 = 0 
    while count <= n:
        ans = n % count
        if ans == 0:
            count2 += 1
            count += 1
        else:
            count +=1
    return count2
n = int(input("Enter n: "))
c = factor_count(n)
print(c)