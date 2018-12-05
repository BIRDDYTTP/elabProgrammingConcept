count = 0
targer = 0
while True:
    num1 = int(input())
    num2 = int(input())
    if num1 <= 0 or num1 >= 7 or num2 <= 0 or num2 >= 7:
        print("ERROR")
        continue
    else:
        if num1+num2==7 or num1+num2==11:
            count += 1
            result = 'W'
            break
        elif num1+num2 == 2 or num1+num2 == 3 or num1+num2 ==12:
            count += 1
            result = 'L'
            break
        else:
            count +=1 
            target = num1 + num2
            while True:
                num3 = int(input())
                num4 = int(input())
                if num3<=0 or num3>=7 or num4<=0 or num4>=7:
                    print('ERROR')
                    continue
                else:
                    if num3+num4==target :
                        count += 1
                        result = 'W'                                   
                        break
                    elif num3+num4 == 7:
                        count +=1
                        result = 'L'
                        break
                    else:
                        count += 1
                        continue
            break      
if count == 1:
    print(count,num1+num2,result)
else:
    print(count,num3+num4,result)