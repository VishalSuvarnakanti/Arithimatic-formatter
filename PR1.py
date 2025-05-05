import re

def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error. Too many problems"

    line1 = []
    line2 = []
    line3 = []

    first = ''
    second = ''
    lines = ''
    sumx = ''
    answer = ''
    
    for part in problems:
        problem = part.split()
        operand1, operator, operand2 = problem
        sum = ""
        if (re.search("[^\s0-9.+-", part)):
            return "Error: Numbers must only contain digits"
        elif (re.search("[/]", part) or re.search("[*]", part)):
            return "Error: Operator must be '+' or '-'"
        elif (len(operand1)>=5 or len(operand2)>=5):
            return "Error: Numbers cannot be more than four digits"
        
        elif operator == "+":
            sum = str(int(operand1) + int(operand2))    
        elif operator == "-":
            sum = str(int(operand1) - int(operand2))
        else:
            return "Error"
        
        length = max(len(operand1), len(operand2))
        top = str(operand1).rjust(length)
        bottom = operator + str(operand2).rjust(length-1)
        line = ""
        result = str(sum).rjust(length)

        for i in range(length):
            line+='-'

        if part != problems[-1]:
            first += top+'    '
            second += bottom+'    '
            lines += line+'    '
            sumx += result+'    '
        else:
            first+=top
            second+=bottom
            lines+=line
            sumx+=result

        if show_answers:
            answer = first + '\n' + bottom + '\n' + lines + '\n' + sumx 
        else:
            answer = first + '\n' + bottom + '\n' + lines

    return answer

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))