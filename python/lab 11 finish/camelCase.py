st = str(input())
st = st.replace('-',' ')
st = st.replace('_',' ')
st = st.replace('=',' ')
st = st.replace('.',' ')
st = st.replace('$',' ')
st = st.title()
st = st.replace(' ','')
a = ''
b = 0
for x in st:
    if b == 0:
        a += x.lower()
    else:
        a += x
    b += 1
print(a)