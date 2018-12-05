passage = str(input())
check = passage.lower()
let = str(input())
count = 0
a = ''
b = ''
while let != '0' and count < 6 :
        let = let.lower()
        ans = check.count(let)
        if ans == 0:
                count += 1
        else:
                check = check.replace(let,'')
                a = a+let
        let = str(input())
for x in passage:
        if (x in a):
                b = b+x
        else:
                b = b+'-'
print(b)