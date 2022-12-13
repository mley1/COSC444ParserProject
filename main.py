
import Fun
import variable
import checkIf
import checkFor
import Booleanops

FoI = ''
FName = ''
sCode = []
aCode = ''
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# The Major Grammar in matrix form
GrammerMajor = [
    [0, 1, 0, 0, 0, 0],  # S (0)
    [0, 0, 1, 0, 0, 0],  # ProgramName (1)
    [0, 0, 1, 1, 1, 1],  # Variables (2)
    [0, 0, 0, 1, 1, 1],  # Procedures (3)
    [0, 0, 0, 1, 1, 1],  # Function (4)
    [0, 0, 0, 0, 0, 1]   # Main (5)
]
currentState = 0


# The following segment will allow the program to read from a file, or read from user input
while True:
    FoI = input("Do you wish to enter a filename? [Y/N]\n")

    if FoI.upper() == "Y":
        FName = input("\nPlease enter your filename(with .txt):\n")
        with open(FName, 'r') as userFile, open('Working.txt', 'w') as workingFile:
            # read content from userFile
            for line in userFile:
                # Write to workingFile
                workingFile.write(line)
        break
    elif FoI.upper() == "N":
        print("Enter you code, you may enter multiple lines, finish by entering an empty line")
        while True:
            user_input = input()
            # if user presses Enter without a value, break out of loop
            if user_input == '':
                break
            else:
                sCode.append(user_input)
        with open(r'Working.txt', 'w') as fp:
            for item in sCode:
                # write each item on a new line
                fp.write("%s\n" % item)
        break
    else:
        continue

content = open(r'Working.txt', 'r').read()
#print("file content:\n" + content)  # TBD

# breaks the file into a list, containing individual characters
charList = []
file = open('Working.txt', 'r')
while True:
    char = file.read(1)
    if not char:
        break
    charList.append(char)
file.close()

#print(charList)  # TBD

# condenses the list into better, more usable parts
condList = []
temp = ''
for x in charList:

    if x.upper() in alphabet:
        temp = temp + x
    else:
        if condList != '':
            condList.append(temp)
        condList.append(x)
        temp = ''
condList.append(temp)
while True:
    if '' in condList:
        condList.remove('')
    else:
        break
#print(condList)  # TBD


workingList =[]
lineChk = True

while True:
    #print('lap')
    workingList = Fun.getToNewLine(condList)
    if len(condList) > 0:
        Fun.removeLine(condList)
        newState = Fun.stateChoose(workingList[0])
    else:
        print('\n Program works')
        break
    if GrammerMajor[currentState][newState] == 1:
        currentState = newState
    else:
        currentState = -1
   # print(f'updated Current State = {currentState}')
    if currentState == -1:
        workingList.remove('\n')
        print(''.join(workingList) + f'{Fun.colors.RED}'
                                                  f'<--Line is out of place in grammar{Fun.colors.ENDC}')
        break
    if currentState == 0:
        print('ERROR')
        break
    elif currentState == 1:
        #print(f'working list = {workingList}')
        lineChk = Fun.parseProgramName(workingList)
        if lineChk:
            workingList.remove('\n')
            print(''.join(workingList))

            #print(f'condList = {condList}')
            #break #TBD
        else:
            print(''.join(workingList) + f'{Fun.colors.RED}ERROR DETECTED{Fun.colors.ENDC}')
            break
    elif currentState == 2:
        workingList.remove('\n')
        print(''.join(workingList))
        guardA = True
        while guardA == True:
            workingList = Fun.getToNewLine(condList)
            #print(condList)
            #print(len(condList))
            if len(condList) > 0:
                Fun.removeLine(condList)
            else:
                print('\n Program works')
                break
            if variable.CheckVar(Fun.spaceDelete(workingList)):
                workingList.remove('\n')
                print(''.join(workingList))
            elif Fun.stateChoose(workingList[0]) != 0:
                print(f'CondList = {condList}')
                print(f'workingList = {workingList}')
                condList = workingList + condList
                print(f'CondList = {condList}')
                guardA = False
            else:
                workingList.remove('\n')
                print(''.join(workingList) + f'{Fun.colors.RED}'
                                             f'<--Line contains an error{Fun.colors.ENDC}')
    elif currentState == 3:
        workingList.remove('\n')
        print(''.join(workingList))
        print(f'{Fun.colors.RED}Procedures Not Yet implemented{Fun.colors.ENDC}')
        break
    elif currentState == 4:
        workingList.remove('\n')
        print(''.join(workingList))
        print(f'{Fun.colors.RED}Functions Not Yet implemented{Fun.colors.ENDC}')
        break
    elif currentState == 5:
        workingList.remove('\n')
        print(''.join(workingList))
        print(f'{Fun.colors.RED}Main Not Yet implemented{Fun.colors.ENDC}')
        break



