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