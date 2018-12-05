ls = []
name_input = input("Enter the student's name : ")
while str.upper(name_input) != 'END': 
    score_input = input("Enter the score : ")
    if float(score_input)>=1 and float(score_input) <= 100:
        ls.append(name_input)
        ls.append(score_input)  
        name_input = input("Enter the student's name : ")
    else:
        break
x = len(ls)
while x > 0:
    print(ls[x-2],ls[x-1])
    x -= 2