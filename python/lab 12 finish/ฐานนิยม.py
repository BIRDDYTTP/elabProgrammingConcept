def find_mode(l) :
    ls = []
    ls2 = []
    ls3 = []
    for i in l :
        if i not in ls :
            ls.append(i)#����� list ��� append ��� i ��� ls 
            ls2.append(l.count(i))#�Ѻ��Ҫԡ� list ��� append ��� ls2
    m = max(ls2) #�����٧�٧ list ls2
    for i in range(len(ls2)) : # ǹ�Ҥ��� ls2
        if m == ls2[i] : # ���͹䢹�� ����� m ���٧�ش � ls2[i] 
            #print(ls2[i])
            print(ls[i] )# ��ԧ�������� ls2 �礤���ҡ�ش ���ԧ ��� ��ͧ�� ls ��� append ������������ 
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
