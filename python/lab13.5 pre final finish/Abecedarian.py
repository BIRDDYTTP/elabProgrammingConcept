st = str(input())
count = 0
st = st.lower()
for x in st:
    if count == 0 :
        a = ord(st[count])
        count += 1
    else:
        b = ord(st[count])
        if b>a:
            a = b
            count += 1
        else:
            break
print(count)