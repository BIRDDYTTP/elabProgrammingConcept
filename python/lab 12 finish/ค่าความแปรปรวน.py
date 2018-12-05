def find_sd(l):
    x = 0
    y = 0
    while x <= len(l)-1:
        b = (ls[x]-(sum(l)/len(l)))**2 
        y += b
        x += 1
    a = (1/len(l)*y)**0.5
    return a
sc = float(input('Enter score: '))
ls = []
while sc != -1 :
    if sc >100 or sc < 0:
        print('Score is out of range.')
    else:
        ls.append(sc)
    sc = float(input('Enter score: '))
if len(ls) == 0:
    pass
else:
    print('Maximum score is %.2f.'%(max(ls)))
    print('Minimum score is %.2f.'%(min(ls)))
    print('Average score is %.2f.'%(sum(ls)/len(ls)))
    print('Standard deviation is %.2f.'%(find_sd(ls)))