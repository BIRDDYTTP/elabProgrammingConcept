def fibo(x):
    if(x>2):
        return fibo(x-1)+fibo(x-2)
    elif x == 0:
        return 0
    else:
        return 1
num = int(input("Enter your number : "))
print(fibo(num))