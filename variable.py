
variableList = []
typeList = []


def isType(typeVal):  # returns bool if input is a type or not
    typeVal = typeVal.upper()
    typelist = ["INTEGER", "REAL", "CHARACTER", "BOOLEAN", "STRING"]
    check = False
    for i in range(5):
        if typeVal == typelist[i]:
            check = True
    return check


def findType(varName):
    for i in range(len(variableList)):
        if varName == variableList[i]:
            return typeList[i]


def typeCheck(typeVal):  # returns int corresponding to the value type
    typeVal = typeVal.upper()
    typelist = ["INTEGER", "REAL", "CHARACTER", "BOOLEAN", "STRING"]
    check = 0
    for i in range(5):
        if typeVal == typelist[i]:
            check = i + 1
    return check


def mismatchCheck(typeVal, varType):  # returns a bool true if type matches, else false
    if not isType(varType):
        for i in range(len(variableList)):
            if varType == variableList[i]:
                varType = typeList[i]
    varType = typeCheck(varType)
    if varType == 0:
        return False
    check = True
    if varType == 1:
        try:
            int(typeVal)
        except ValueError:
            check = False
    if varType == 2:
        try:
            float(typeVal)
        except ValueError:
            check = False
    if varType == 3 and not len(typeVal) == 1:
        check = False
    if varType == 4 and not (typeVal.upper() == 'TRUE' or typeVal.upper() == 'FALSE'):
        check = False
    if varType == 5 and not len(typeVal) > 1:
        check = False
    return check


def isName(nameVal):  # returns a bool true if varname is within pascal alphabet, else false
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
        check = False
        return check
    for i in range(len(varList) - 1):
        if varList[i] == ':':
            colonCheck += 1
            if colonCheck > 1:
                check = False
                return check
        elif varList[i] == ';':
            semiCheck += 1
            if semiCheck > 1:
                check = False
                return check
        elif varList[i] == '=':
            equalCheck += 1
            if equalCheck > 1:
                check = False
                return check
        elif varList[i] == ',':
            commaCheck += 1
            if commaCheck >= 1:
                multiVar = True
    if not multiVar:
        valueType = 0
        if len(varList) > 8:
            valueType = typeCheck(varList[2])
        if len(varList) > 5:
            if not isName(varList[0]):
                check = False
            if varList[1] != ':':
                check = False
            if not isType(varList[2]):
                check = False
            if not varList[3] == '=':
                check = False
            if valueType == 3 or valueType == 5:
                if not (varList[4] == "'" and varList[6] == "'"):
                    check = False
                if not mismatchCheck(varList[5], varList[2]):
                    check = False
                if not varList[len(varList)-2] == ';':
                    check = False
            else:
                if not mismatchCheck(varList[4], varList[2]):
                    check = False
                if not varList[5] == ';':
                    check = False
            if check:
                variableList.append(varList[0])
                typeList.append(varList[2])
        else:
            if not isName(varList[0]):
                check = False
            if varList[1] != ':':
                check = False
            if not isType(varList[2]):
                check = False
            if varList[3] != ';':
                check = False
            if check:
                variableList.append(varList[0])
                typeList.append(varList[2])
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
        if check:
            for i in range(0, len(varList) - 4, 2):
                variableList.append(varList[i])
                typeList.append(varList[len(varList) - 3])
    return check


def CheckVarAssignment(varStmt):  # returns bool true if var assignment statement is valid, else false
    check = True
    if not isName(varStmt[0]):
        check = False
    if not varStmt[1] == '=':
        check = False
    if not mismatchCheck(varStmt[2], varStmt[0]):
        check = False
    if not varStmt[3] == ';':
        check = False
    return check


def declaredVarTest(passedVar):  # returns bool true if passed var name is within variable list, else false
    #print(variableList)
    for x in variableList:
        if passedVar == x:
            return True
    return False


# test = ['a', ':', 'integer', ';', '\n']
# test2 = ['a', '=', 'abc', ';', '\n']

# print(CheckVar(test))
# print(CheckVarAssignment(test2))
# print(declaredVarTest('a')) #must be run after CheckVar for the variable name to be in the list
