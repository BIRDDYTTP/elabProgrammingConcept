num = input()
if len(num) != 4:
    print('ERROR')
else:
    if num[1].isdigit() == False and num[1].isalpha() == False:
        print('ERROR')
    else:
        if num[1].isdigit() == True:
            ans = int(num[0]) * int(num[2:])
        elif num[1].isalpha() == True:
            ans = int(num[0]) ** int(num[2:])
print(ans)