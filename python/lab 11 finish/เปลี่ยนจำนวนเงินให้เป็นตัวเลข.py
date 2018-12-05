money = str(input())
dot_amount = money.count('.')
ans = ''
dot = ''
if dot_amount > 1 :
    ans = 'ERROR'
else:
    dot_point = money.find('.')
    count = 0
    for x in money[dot_point:]:
        count += 1
        dot += x
    if count == 3 or dot_point == -1:
        check_int = ''
        for x in money:
            if x =='.':
                break
            else:
                check_int += x
        count2 = len(check_int)
        count3 = 0
        count4 = 1
        if count2 == 0:
            ans = 'ERROR'
        elif check_int.count(',') == 0:
            while count2 > 0:
                if count4 % 4 != 0:
                    if check_int[-1-(count3)].isdigit() == True:
                        ans += check_int[-1-count3]
                    else:
                        ans = 'ERROR'
                        break
                    count2 -= 1
                    count3 += 1
                    count4 += 1
                elif count4 % 4 == 0:
                    if check_int[-1-count3].isdigit() == True:
                        ans += check_int[-1-count3]
                    else:
                        ans = 'ERROR'
                        break
                    count2 -= 1
                    count3 += 1
                    count4 += 1
                else:
                    ans = 'ERROR'
                    break            
            
        else:
            while count2 > 0:
                if count4 % 4 != 0:
                    if check_int[-1-(count3)].isdigit() == True:
                        ans += check_int[-1-count3]
                    else:
                        ans = 'ERROR'
                        break
                    count2 -= 1
                    count3 += 1
                    count4 += 1
                elif count4 % 4 == 0:
                    if check_int[-1-count3] == ',':
                        ans += check_int[-1-count3]
                    else:
                        ans = 'ERROR'
                        break
                    count2 -= 1
                    count3 += 1
                    count4 += 1
                else:
                    ans = 'ERROR'
                    break

    else:
        ans = 'ERROR'
for x in dot:
    if x !='.' and x.isdigit() != True:
        ans ='ERROR'
        dot = ''
if ans[len(ans)-1] == ',':
    ans = 'ERROR'
if ans != 'ERROR':
    ans = ans.replace(',','')
    ans = ans[-1::-1]
    ans = int(ans) + 1
    ans = str(ans)    
    ans += dot
    if ans.count('.') == 0 :
        ans = int(ans)-int(dot)
        ans = (str(ans))
        ans = ans[0:len(ans)-1]
print(ans)