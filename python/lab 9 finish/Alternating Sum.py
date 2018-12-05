def summ(n):
    x = 1
    zero = 0
    while x <= n:
        if x%2 == 0:
            zero -= x
            x += 1
        else:
            zero += x
            x += 1
    return zero
n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to %d is %d" % (n,summ(n)))