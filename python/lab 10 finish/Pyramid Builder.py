num = int(input())
count = 1
while count <= num:
        print('|'+(' '*(num-count))+('*'*(2*count-1))+(' ' *(num-count))+'|')
        count += 1