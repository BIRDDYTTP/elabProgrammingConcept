def month(a):
    b = a[3:]
    if int(b) < 1 or int(b) > 12:
        return 'Wrong Month'
    else:
        return int(b)
def day(a,c):
    b = a[0:2]
    if c == 'Wrong Month':
        if int(b) < 1 or int(b) > 31:
            return 'Wrong Day'
    else:
        if c == 1 or c == 3 or c == 5 or c == 7 or c == 8 or c == 10 or c == 12 :
            if int(b) < 1 or int(b) > 31:
                return 'Wrong Day'
            else:
                return int(b)
        elif c == 2:
            if int(b) < 1 or int(b) > 28:
                return 'Wrong Day'
            else:
                return int(b)
        else:
            if int(b) < 1 or int(b) > 30:
                return 'Wrong Day'
            else:
                return int(b)
def checkd(c):
    if c == 1 or c == 3 or c == 5 or c == 7 or c == 8 or c == 10 or c == 12 :
        return 31
    elif c == 2:
        return 28
    else:
        return 30
d1 = str(input())
d2 = str(input())
first = int(input())
rs1 = month(d1)
rs2 = month(d2)
chc1 = day(d1,rs1)
chc2 = day(d2,rs2)
if rs1 == 'Wrong Month' or rs2 == 'Wrong Month' or chc1 == 'Wrong Day' or chc2 == 'Wrong Day' or first < 1 or first > 7:
    if rs1 == 'Wrong Month' or rs2 == 'Wrong Month' :
        print('Wrong Month')
    if chc1 == 'Wrong Day' or chc2 == 'Wrong Day' or first <1 or first > 7:
        print('Wrong Day')
else:
    countsun = 0
    if rs1 == rs2 :
        days = checkd(rs1)
        while first <= days:
            if (first >= chc1 and first <= chc2) or (first >= chc2 and first <= chc1):
                countsun += 1
                first += 7
            else:
                first += 7
    else:
        mm = max([rs1,rs2])
        mmm = min([rs1,rs2])
        count = 1
        dayy = 0
        if mmm == rs1:
            sec = chc1
            sec2 = chc2
        else:
            sec = chc2
            sec2 = chc1
        while count <= mm :
            first += dayy
            days = checkd(count)
            while first <= days:
                if count >= mmm and count <= mm:
                    if count == mmm:
                        if first >= sec:
                            countsun += 1
                            first += 7
                        else:
                            first += 7
                    elif count == mm:
                        if first <= sec2:
                            countsun += 1
                            first += 7
                        else:
                            first += 7
                    else:
                        countsun += 1
                        first += 7
                else:
                    first += 7
            
            dayy = (first-days)-1
            first = 1
            count += 1
    print(countsun)