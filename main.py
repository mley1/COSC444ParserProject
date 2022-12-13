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
# Checks for boolean operation.
#########################################################
def CheckBooleanOperator(left, operator, right):
    if operator == '<':
        if left < right:
            return True
        else:
            return False
    if operator == '>':
        if left > right:
            return True
        else:
            return False
    if operator == '=':
        if left == right:
            return True
        else:
            return False
    if operator == '<>':
        if left != right:
            return True
        else:
            return False


#########################################################
# Checks for boolean expression.
#########################################################
def CheckBooleanExpression(condition_list):
    if len(condition_list) == 1:
        # if (exit) then
        if condition_list[0] == True:
            return True
        else:
            return False

    if len(condition_list) == 3:
        left = condition_list[0]
        operator = condition_list[1]
        right = condition_list[2]
        return CheckBooleanOperator(left, operator, right)
    if len(condition_list) == 4:
        left = condition_list[0]
        operator = condition_list[1] + condition_list[2]
        right = condition_list[3]
        return CheckBooleanOperator(left, operator, right)

#########################################################
# Checks for if statements.
#########################################################
def CheckIf(condList):

    condition_list = []
    true_false_list = []
    is_if = False
    is_and = False
    is_or = False
    for x in condList:
        if x == ' ':
            continue
        if x.upper() == "AND":
            is_and = True
            condition_list = []
            continue
        if x.upper() == "OR":
            is_or = True
            condition_list = []
            continue
        if x == ")" or x.lower() == "then":
            result_boolean = CheckBooleanExpression(condition_list)
            true_false_list.append(result_boolean)

            condition_list = []
            if x.lower() == ")":
                if is_and:
                    and_result = true_false_list[0] and true_false_list[1]
                    true_false_list = [and_result]
                    is_and = False
                if is_or:
                    or_result = true_false_list[0] or true_false_list[1]
                    true_false_list = [or_result]
                    is_or = False
            if x.lower() == "then":
                is_if = False
                if len(true_false_list) == 2:
                    if is_and:
                        and_result = true_false_list[0] and true_false_list[1]
                        true_false_list = [and_result]
                        is_and = False
                    if is_or:
                        or_result = true_false_list[0] or true_false_list[1]
                        true_false_list = [or_result]
                        is_or = False
                return true_false_list[0]

        if x == "(":
            continue
        if is_if == True:
            condition_list.append(x)
        if x.lower() == "if":
            is_if = True


print(CheckIf(condList))

#########################################################
# returns a list of begin end statements
#########################################################
def BeginEnd(condList):
    beginCount = 0
    endCount = 0
    resultList = []
    beginEndList = []
    for word in condList:
        if word.lower() == "begin":
            beginCount += 1
            beginEndList.append(word)
        elif word.lower() == "end":
            endCount += 1
            beginEndList.append(word)
            if beginCount == endCount:
                resultList.append(beginEndList)
                beginCount = 0
                endCount = 0
                beginEndList = []
        else:
            if beginCount > 0:
                beginEndList.append(word)
    return resultList

