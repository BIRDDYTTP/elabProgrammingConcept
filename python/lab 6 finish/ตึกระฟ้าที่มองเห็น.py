count = 0
tall = 0
while True:
    inp_tall = int(input())
    if inp_tall > tall:
        count = count+1
        tall = inp_tall
        continue
    elif inp_tall == -1:
        break
    else:
        pass
        continue
print(count)