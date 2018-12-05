frame = 1
score = 0
while frame <= 10:
    print("Frame # %d" %frame)
    pindown = int(input("  Number of pins down: "))
    if pindown == 10:
        score = score + 10
        frame = frame + 1
        continue
    elif pindown>=0 and pindown <10:
        pinnodown = 10 - pindown
        print("Frame # %d" %frame)
        pindown2 = int(input("  Number of pins down (0-%d): " %pinnodown))
        score  = pindown + pindown2 + score
        frame = frame + 1
        continue
print("Total score is %d"%score)        