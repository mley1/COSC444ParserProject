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
    States = ['program', 'var'];

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
def parseProgramName(inputList):
    parseList = inputList.copy()
    while True:
        if ' ' in parseList:
            parseList.remove(' ')
        else:
            break
    #print(f'remove whitespace = {parseList}')
    if parseList[0] == 'program' and str(parseList[1]) and parseList[2] == ';' and parseList[3] == '\n':
        return True
    else:
        return False
def removeLine(inputList):
    while True:
        if inputList[0] != '\n':
            del inputList[0]
        else:
            del inputList[0]
            break
