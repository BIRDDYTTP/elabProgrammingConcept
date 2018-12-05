def checkunit(n):
    a = ''
    if n == 1:
        a += 'one'
    elif n == 2:
        a += 'two'
    elif n == 3:
        a += 'three'
    elif n == 4:
        a += 'four'
    elif n == 5:
        a += 'five'
    elif n == 6:
        a += 'six'
    elif n == 7:
        a += 'seven'
    elif n == 8:
        a += 'eight'
    elif n == 9:
        a += 'nine'
    elif n == 0:
        a += 'zero'
    return a
def checkten(n):
    a =''
    if n == 10:
        a += 'ten'
    elif n == 11:
        a += 'eleven'
    elif n == 12:
        a += 'twelve'
    elif n == 13:
        a += 'thirteen'
    elif n == 14:
        a += 'fourteen'
    elif n == 15:
        a += 'fifteen'
    elif n == 16:
        a += 'sixteen'
    elif n == 17:
        a += 'seventeen'
    elif n == 18:
        a += 'eighteen'
    elif n == 19:
        a += 'nineteen'
    else:
        count = 1
        for x in str(n):
            if count == 1:
                if x == '2':
                    a += 'twenty'
                elif x == '3':
                    a += 'thirty'
                elif x == '4':
                    a += 'forty'
                elif x == '5':
                    a += 'fifty'
                elif x == '6':
                    a += 'sixty'
                elif x == '7':
                    a += 'seventy'
                elif x == '8':
                    a += 'eighty'
                elif x == '9':
                    a += 'ninety'
            elif count == 2:
                if x == '1':
                    a += '-one'
                elif x == '2':
                    a += '-two'
                elif x == '3':
                    a += '-three'
                elif x == '4':
                    a += '-four'
                elif x == '5':
                    a += '-five'
                elif x == '6':
                    a += '-six'
                elif x == '7':
                    a += '-seven'
                elif x == '8':
                    a += '-eight'
                elif x == '9':
                    a += '-nine'
            count += 1
    return a
def checkhun(n):
    a = ''
    count = 1
    for x in str(n):
        if count == 1:
            if x == '1':
                a += 'one'
            elif x == '2':
                a += 'two'
            elif x == '3':
                a += 'three'
            elif x == '4':
                a += 'four'
            elif x == '5':
                a += 'five'
            elif x == '6':
                a += 'six'
            elif x == '7':
                a += 'seven'
            elif x == '8':
                a += 'eight'
            elif x == '9':
                a += 'nine'
            a += '-hundred'
        elif count == 2:
            if x == '2':
                a += 'twenty'
            elif x == '3':
                a += 'thirty'
            elif x == '4':
                a += 'forty'
            elif x == '5':
                a += 'fifty'
            elif x == '6':
                a += 'sixty'
            elif x == '7':
                a += 'seventy'
            elif x == '8':
                a += 'eighty'
            elif x == '9':
                a += 'ninety'
            elif x == '1':
                if str(n)[1:] == '10':
                    a += '-ten'
                elif str(n)[1:] == '11':
                    a += '-eleven'
                elif str(n)[1:] == '12':
                    a += '-twelve'
                elif str(n)[1:] == '13':
                    a += '-thirteen'
                elif str(n)[1:] == '14':
                    a += '-fourteen'
                elif str(n)[1:] == '15':
                    a += '-fifteen'
                elif str(n)[1:] == '16':
                    a += '-sixteen'
                elif str(n)[1:] == '17':
                    a += '-seventeen'
                elif str(n)[1:] == '18':
                    a += 'eighteen'
                elif str(n)[1:] == '19':
                    a += '-nineteen'
                count += 1
        elif count == 3:
            if x == '1':
                a += '-one'
            elif x == '2':
                a += '-two'
            elif x == '3':
                a += '-three'
            elif x == '4':
                a += '-four'
            elif x == '5':
                a += '-five'
            elif x == '6':
                a += '-six'
            elif x == '7':
                a += '-seven'
            elif x == '8':
                a += '-eight'
            elif x == '9':
                a += '-nine'
        count += 1            
    return a
num = int(input())
if len(str(num)) == 1:
    print(checkunit(num))
elif len(str(num)) == 2:
    print(checkten(num))
elif len(str(num)) == 3:
    print(checkhun(num))
else:
    print('ERROR')