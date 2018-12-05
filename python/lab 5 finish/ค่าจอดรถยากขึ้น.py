num = input()
count = 1
Sum = 0
if num != '':
    while num != '':
        if count == 1:
            maxNum = float(num)
            minNum = float(num)
            count += 1
        else:
            if float(num) > maxNum:
                maxNum = float(num)
            elif float(num) < minNum:
                minNum = float(num)
            count += 1
        Sum += float(num)
        num = input()
    print("%.2f %.2f" %(minNum,maxNum))
    print("%.2f %.2f" %(Sum,(Sum/count)))