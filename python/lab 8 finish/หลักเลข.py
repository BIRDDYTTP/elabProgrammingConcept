def digit(num):
    a = num%10
    return a
def tens(num):
    a = (num//10)%10
    return a
def hundreds(num):
    a = ((num//10)//10)%10
    return a
def thousands(num):
    a = (((num//10)//10)//10)%10
    return a
def sum_digits(num):
    x = 1
    y = 0
    while x <= 4:
        a = num%10
        y += a
        x += 1
        num = num //10
    return y
n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))