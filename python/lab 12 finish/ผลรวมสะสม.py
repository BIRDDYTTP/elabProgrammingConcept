def accum_sum(l):
    a = []
    b = 0
    for x in range(len(l)):
        b = b+l[x]
        a.append(b)
    for b in a:
        print(b)
num = int(input('Enter a number (0 to end): '))
numls = []
while num != 0:
    if num < 1 or num > 999:
        print('Number is out of range.')
    else:
        numls.append(num)
    num = int(input('Enter a number (0 to end): '))
print('Original list:')
print(numls)
print('Accumulative Sum:')
a = accum_sum(numls)