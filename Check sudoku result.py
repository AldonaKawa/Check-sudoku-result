import sys

def checkUniq(listIN):
    #check if list is uniqe
    return len(listIN) == len(set(listIN))
    
def CheckHorizontalLines(listIN):
    #check horizontal lines   
    NonUniq = 0
    
    for i in helpList:
        if checkUniq(i) == False:
            NonUniq = 1

    if NonUniq > 0:
        return False
    else:
        return True

def CheckVerticalLines(listIN):
    #check vertical lines 
    NonUniq = 0
    
    for i in range(len(listIN)):
        hArray = []
        for j in range(len(listIN[i])):
            hArray.append(listIN[j][i])
        if checkUniq(hArray) == False:
            NonUniq = 1

    if NonUniq > 0:
        return False
    else:
        return True
    
def CheckSquares(listIN):
    #check Squares
    NonUniq = 0
    k = 0
    l = 0
    
    for x in range(9): #9 squares
        hArray = []
        for i in range(3):
            for j in range(3):
                if l > 8: #max 9 lines
                    l = 0
                hArray.append(listIN[i+k][j+l]) 
        l = l + 3
        if (x+1)%3 == 0:
            k = k + 3
            
        if checkUniq(hArray) == False:
            NonUniq = 1

        if NonUniq > 0:
            return False
        else:
            return True


sudokuList = []

#Enter the numbers manually

##for i in range(9):
##     linia = input('Wprowadź '+ str(i+1) + ' wiersz\n')
##     while linia.isdigit() == False or len(linia) != 9:
##         linia = input('Niepoprawne dane, wprowadź '+ str(i+1) + ' wiersz\n')
##     sudokuLista.append(linia)


#Enter the numbers manually into the script
sudokuList.append('295743861')
sudokuList.append('431865927')
sudokuList.append('876192543')
sudokuList.append('387459216')
sudokuList.append('612387495')
sudokuList.append('549216738')
sudokuList.append('763524189')
sudokuList.append('928671354')
sudokuList.append('154938672')

#convert every line to list
helpList = []
for i in sudokuList:
    helpList.append(list(i))
    
#check horizontal lines
if CheckHorizontalLines(helpList) == False:
    print('No')
    sys.exit()


#check vertical lines
if CheckVerticalLines(helpList) == False:
    print('No')
    sys.exit()

#check squares
if CheckSquares(helpList) == False:
    print('No')
    sys.exit()
else: #If everything is OK
    print('Yes')
