def isType(typeVal):
    typeVal = typeVal.upper()
    typeList = ["INTEGER", "REAL", "CHARACTER", "BOOLEAN", "STRING"]
    check = False
    for i in range(5):
        if typeVal == typeList[i]:
            check = True
    return check


def isName(nameVal):
    check = False
    nameVal = nameVal.upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for x in range(len(nameVal)):
        if not nameVal[x] in alphabet:
            check = False
        else:
            check = True
    return check


def CheckVar(varList):
    multiVar = False
    check = True
    spaceList = []
    colonCheck = 0
    semiCheck = 0
    equalCheck = 0
    commaCheck = 0

    for i in range(len(varList)):
        if varList[i] == ' ':
            spaceList.append(i)
    for i in range(len(spaceList)):
        if varList[spaceList[i] - i] == ' ':
            varList.pop(spaceList[i] - i)

    if varList[len(varList) - 2] != ';':
        #print(';')
        check = False
        return check
    for i in range(len(varList) - 1):
        if varList[i] == ':':  # Checks for more than 1 colon
            colonCheck += 1
            if colonCheck > 1:
                check = False
                return check
        elif varList[i] == ';':  # Checks for more than 1 semicolon
            semiCheck += 1
            if semiCheck > 1:
                check = False
                return check
        elif varList[i] == '=':  # Checks for more than 1 equals
            equalCheck += 1
            if equalCheck > 1:
                check = False
                return check
        elif varList[i] == ',':  # Checks for more than 1 comma
            commaCheck += 1
            if commaCheck >= 1:
                multiVar = True
    if not multiVar:
        if len(varList) > 5:
            if not isName(varList[0]):
                check = False
            if varList[1] != ':':
                check = False
            if not isType(varList[2]):
                check = False
            if not varList[3] == '=':
                check = False
            if not varList[5] == ';':
                check = False
        else:
            if not isName(varList[0]):
                check = False
            if varList[1] != ':':
                check = False
            if not isType(varList[2]):
                check = False
            if varList[3] != ';':
                check = False
    if multiVar:
        for i in range(0, len(varList) - 5, 2):
            if not isName(varList[i]):
                check = False
        if not isName(varList[len(varList) - 5]):
            check = False
        for i in range(1, len(varList) - 6, 2):
            if not varList[i] == ',':
                check = False
        if not varList[len(varList) - 4] == ':':
            check = False
        if not isType(varList[len(varList) - 3]):
            check = False
        if not varList[len(varList) - 2] == ';':
            check = False
    return check


# not fully implemented
def CheckVarAssignment(varStmt):
    check = True
    if not isName(varStmt[0]):
        check = False
    if not varStmt[1] == ':':
        check = False
    # check if value is valid here
    if not varStmt[3] == ';':
        check = False
    return check


# name = value ;