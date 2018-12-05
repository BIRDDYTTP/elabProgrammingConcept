st = str(input())
z = st.count(',')+1
x = ''
count = 1
while count <= z:
    a = ''
    for y in st :
        if y == ',':
            break
        else:
            a = a+y
    st = st.replace(a+',','')
    if count < z:
        a = '"'+a.strip()+'"'+','
        x = x+a
        count += 1
    else:
        a = '"'+a.strip()+'"'
        x = x+a
        count += 1
print(x)