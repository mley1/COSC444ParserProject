class colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def stateChoose(input):
    States = ['program', 'var', 'procedure', 'function', 'begin'];
    input = input.lower()
    if input in States:
        return (States.index(input)+1)
    else:
        return 0


def getToNewLine(inputList):
    newList = []

    for x in inputList:
        if x != '\n':
            newList.append(x)
            #print(f'! {newList}')
        else:
            newList.append(x)
            #print(newList)
            return newList


def spaceDelete(inputList):
    if inputList is not None:
        parseList = inputList.copy()
    else:
        return inputList
    while True:
        if ' ' in parseList:
            parseList.remove(' ')
        else:
            break
    return parseList


def parseProgramName(inputList):
    parseList = spaceDelete(inputList)
    if parseList[0] == 'program' and str(parseList[1]) and parseList[2] == ';' and parseList[3] == '\n':
        return True
    else:
        return False


def removeLine(inputList):
    while True:
        if len(inputList) == 0:
            break
        elif inputList[0] != '\n':
            del inputList[0]
        else:
            del inputList[0]
            break
