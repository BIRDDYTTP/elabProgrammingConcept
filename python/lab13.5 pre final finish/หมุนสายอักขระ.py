s = str(input())
num = int(input())
st = ''
if num > 0 :
    num = num * (-1)
    st = st+s[num:]
    s = s[len(s)*(-1):num]
    st = st + s
elif num < 0:
    num = (num *(-1))%len(s)
    st = st + s[num:len(s)]
    s = s[0:num]
    st = st + s
else:
    st = s
print(st)
