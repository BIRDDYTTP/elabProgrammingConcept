target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
digitCorrect = 0
indexCorrect = 0
targetIndex = 0
while target > 0:
    targetNumber = target%10
    guessIndex = 0
    guessingNum = guess
    while guessingNum > 0:
        guessNumber = guessingNum%10
        if guessIndex == targetIndex:
            if targetNumber == guessNumber:
                indexCorrect +=1
                break
        else:
            if targetNumber == guessNumber:
                digitCorrect += 1
        guessIndex +=1
        #print("digit %d index %d"%(digitCorrect ,indexCorrect))
        #print(targetNumber, guessNumber)
        guessingNum = guessingNum//10
    target = target//10
    targetIndex+=1
#print(digitCorrect, indexCorrect)
if (indexCorrect == 4):
    print("Congratulations, you just mastered my mind!!")
else:
    if (indexCorrect == 0):
        indexOut = "No positions correct,"
    elif (indexCorrect == 1):
        indexOut = "One position correct,"
    elif (indexCorrect == 2):
        indexOut = "Two positions correct,"
    elif (indexCorrect == 3):
        indexOut = "Three positions correct,"
    if (digitCorrect == 0):
        digitOut = " no digits correct"
    elif (digitCorrect == 1):
        digitOut = " one digit correct"
    elif (digitCorrect == 2):
        digitOut = " two digits correct"
    elif (digitCorrect == 3):
        digitOut = " three digits correct"
    elif (digitCorrect == 4):
        digitOut = " four digits correct"
    print(indexOut+digitOut)