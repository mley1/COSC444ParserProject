
def isType(typeVal):
    typeList = ["Integer", "Real", "Character", "Boolean", "String"]
    check = False
    for i in range(5):
        if typeVal == typeList[i]:
            check = True
    return check


def isName(nameVal):
    check = False
    nameVal.upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for x in nameVal:
        if not nameVal[x] in alphabet:
            check = False
    return check


def CheckVar(varList):
    multiVar = False
    check = True
    colonCheck = 0
    semiCheck = 0
    equalCheck = 0
    commaCheck = 0

    if varList[len(varList)-2] != ';':
        check = False
        return check
    for i in range(len(varList)):
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
        elif varList[i] == ' ':
            varList.pop(i)
        else:
            if varList[i] == ',':  # Checks for more than 1 comma
                commaCheck += 1
                if commaCheck > 1:
                    multiVar = True
    if not multiVar:
        if varList[1] != ':':
            check = False
        if varList[3] != '=':
            check = False
    if multiVar:
        for i in range(0, len(varList) - 3, 2):
            if not isName(varList[i]):
                check = False
        for i in range(1, len(varList) - 4, 2):
            if not varList[i] == ',':
                check = False
        if not isType(varList[len(varList) - 2]):
            check = False
    return check


# varname : type ;
# varname : type = value;

# varname := value; post declaration assignment/reassignment outside scope of this function
