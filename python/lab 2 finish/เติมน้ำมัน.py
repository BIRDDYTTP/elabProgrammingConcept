import math
distance = int(input())
capacity = int(input())
kaew = ((distance/15)/(capacity/2))+1
khwan = ((distance/15)/(9*capacity/10))+1
e = math.floor(kaew)
f = math.floor(khwan)
print(e)
print(f)