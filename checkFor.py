#########################################################
# Checks for the validity of a For Loop                 #
#########################################################
def checkFor(inputList):
    currentValue = 0
    shortList = []
    j= 0

    # Create a temporary list that excludes all white spaces from the inputted condList
    for i in range(len(inputList)):
        if inputList[i] != ' ':
            shortList[j] = inputList[i]
            j = j+1
            break
        break

    for i in range(len(shortList)):
        if i == 0 and shortList[i] == 'for':
            currentValue = 1
        else:
            currentValue = 0
        if i == 4 and shortList[i] == 'to':
            currentValue = 1
        else:
            currentValue = 0
        if i == 6 and shortList[i] == 'do':
            currentValue = 1
        else:
            currentValue = 0

    if currentValue == 1:
        return True
    else:
        return False








