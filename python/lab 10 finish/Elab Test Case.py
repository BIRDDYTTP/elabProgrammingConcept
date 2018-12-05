result = str(input())
x = result.upper()
a = str(input())
check = a.upper()
count = 0
for letter in check:
    ans = x.count(letter)
    count += ans
    x = x.replace(letter,'')
print(count)
if len(result)-2 > 0:
    print('%.2f'%(count/(len(result)-2)*100))
else:
    print('0.00')