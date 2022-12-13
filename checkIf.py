import Booleanops
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
            result_boolean = Booleanops.CheckBooleanExpression(condition_list)
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


#print(CheckIf(condList))
