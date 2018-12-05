# ----- FUNCTION PART ----- #

def isValidInput(dimension, delimiter) : 
    # Check Input : intxint or int,int
    # example of delimiter : 'x' or ',' or etc.
    
    temp = dimension.split(delimiter)
    
    if temp[0].isdigit and temp[1].isdigit :
        if int(temp[0]) > 0 and int(temp[1]) > 0 :
            return True
    return False

def create2DList(i,j) :
    # Create 2D List with initialize value 0
    # list[i][j]
    
    ls = []
    for outer in range(i) :
        ls.append([])
        for inter in range(j) :
            ls[outer].append(0)

    return ls

def inputBomb(list2D) :
    # Input Bomb to list
    # list[i][j]
    
    temp = input()
    while isValidInput(temp, ',') :
        if int(temp[0]) < 0 or int(temp[0]) > len(list2D)-1 :
            print("Out of Range : i")
            temp = input()
            continue
        if int(temp[2]) < 0 or int(temp[2]) > len(list2D[0])-1 :
            print("Out of Range : j")
            temp = input()
            continue
        
        list2D[int(temp[0])][int(temp[2])] = '*'
        return # Use to force-out of function
        
def findBomb(ls, outer, inner) :
    # Count Bomb around ls[outer][inner]
    # Count's value can't exceed 9
    
    lenOuter = outer-1
    lenInner = inner-1
    count = 0
    
    for i in range(lenOuter, outer+2) :
        if i < 0 or i > len(ls)-1 :
            pass
        else : 
            for j in range(lenInner, inner+2) :
                if j < 0 or j > len(ls[outer])-1 :
                    pass
                else :
                    if ls[i][j] == '*' :
                        count += 1
            
    ls[outer][inner] = count
    
def print2D(ls) :
    for i in ls :
        for j in i :
            print(j, end='')
        print()

# ----- END OF FUNCTION PART ----- #


# START OF MAIN PROGRAM

dimension = input()

if isValidInput(dimension, 'x') :
    i = int(dimension.split('x')[0])
    j = int(dimension.split('x')[1])
    
    table = create2DList(i, j)
    #print(table)
    
    numBomb = int(input())
    if numBomb < 0 or numBomb > i*j :
        print("Out of Range : total")
    else :
        for p in range(numBomb) :
            inputBomb(table)
        
        #print(table)
        
        for outer in range(len(table)) :
            for inner in range(len(table[outer])) :
                if table[outer][inner] != '*' :
                    findBomb(table, outer, inner)
                
        print2D(table)
else :
    print("Out of Range : dimension")