
def check_order(l):
    if len(l) == 0:
        return 'The list is empty.'
    else:
        a = []
        a = a+l
        b = []
        b = b+l
        a.sort()
        b.sort(reverse = True)
        if l == a and l == b:
            return 'The list is in non-increasing and non-decreasing order.'
        elif l == b:
            return 'The list is in non-increasing order.'
        elif l == a :
            return 'The list is in non-decreasing order.'
        else:
            return 'The list is in random order.'
ls = []
num = int(input('Enter a number (-1 to end): '))
while num != -1 :
    if num > 100 or num < 0:
        print('Number is out of range.')
    else:
        ls.append(num)
    num = int(input('Enter a number (-1 to end): '))
print('-----')
print('Original list:')
print(ls)
print(check_order(ls))