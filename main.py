

FoI = ''
FName = ''
sCode = []
aCode = ''
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

        #code here should move the text found in the file to the variable sCode

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

content = open(r'Working.txt', 'r').read()
print("file content:\n" + content)
#Actual parsing begins
