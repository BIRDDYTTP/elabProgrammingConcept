Item = int(input())
use = Item // 3
use2 = Item%3
if use!=0 and use2==0:
    total = use*(15+19+12)
    total2 = 0
if use2 == 1:
    total = use*(15+19+12)
    total2 = 15
elif use2 == 2:
    total = use*(15+19+12)
    total2 = 19+15
alltotal = total+total2
print(alltotal)