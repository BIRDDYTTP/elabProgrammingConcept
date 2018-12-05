def find_mode(l) :
    ls = []
    ls2 = []
    ls3 = []
    for i in l :
        if i not in ls :
            ls.append(i)#ไว้เช็ค list ที่ append ค่า i เข้า ls 
            ls2.append(l.count(i))#นับสมาชิกใน list และ append เข้า ls2
    m = max(ls2) #เช็ค่าสูงสูง list ls2
    for i in range(len(ls2)) : # วนหาค่าใน ls2
        if m == ls2[i] : # เงื่อนไขนี้ จะให้ m เช็คสูงสุด ใน ls2[i] 
            #print(ls2[i])
            print(ls[i] )# จริงอยู่ที่ใช้ ls2 เช็คค่ามากสุด ก็จริง แต่ก็ ต้องใช้ ls ที่ append ค่าเดิมเอาไว้ 
    #print(ls)
    #print(ls2)
l = []
count = 0
while count < 20 :
    score = int(input('Enter score: '))
    if score < 0 or score > 10 :
        print('Score is out of range.')
    else:
        l.append(score)
        count += 1

print('-----')
print('Original list:')
print(l)
print('Mode of scores:')
find_mode(l)
