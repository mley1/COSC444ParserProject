
FoI = ''
FName = ''
sCode = []
aCode = ''
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1'
    ,'2','3','4','5','6','7','8','9','0']
#The following segment will allow the program to read from a file, or read from user input
while True:
    FoI = input("Do you wish to enter a filename? [Y/N]\n")

    if FoI.upper() == "Y":
        FName = input("\nPlease enter your filename(with .txt):\n")
        with open(FName,'r') as userFile, open('Working.txt','w') as workingFile:
            #read content from userFile
            for line in userFile:
                #Write to workingFile
                workingFile.write(line)
        break
    elif FoI.upper() == "N":
        print("Enter you code, you may enter multiple lines, finish by entering an empty line")
        while True:
            user_input = input()
            #if user presses Enter without a value, break out of loop
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

content = open(r'Working.txt', 'r').read() #TBD
print("file content:\n" + content) #TBD

#breaks the file into a list, containing individual characters
charList = []
file = open('Working.txt','r')
while True:
    char = file.read(1)
    if not char:
        break
    charList.append(char)
file.close()
print(charList) #TBD

#condenses the list into better, more usable parts
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
print(condList) #TBD


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
            break;
        break

    for i in range(len(shortList)):
         if i/2 ==0:
             if shortList [i] == 'for' or shortList [i] == ':=' or shortList [i] == 'to' or shortList [i] == 'do' or shortList [i] == ':'
                 currentValue = 1
        else:
            currentValue = 0
    if currentValue == 1:
        return True
    else:
        return False








