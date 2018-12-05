passage = str(input())
check = passage.upper()
let = str(input())
count = 0
while let != '0':
        let = let.upper()
        ans = check.count(let)
        count += ans
        check = check.replace(let,'')
        let = str(input())
print('%d/%d'%(count,len(passage)))