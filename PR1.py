import re

#def print_lines(line1, line2, line3, show_answers):
#    newline1 = [str(i) for i in line1]
#    newline2 = [str(i) for i in line2]
#    newline3 = [str(i) for i in line3]
#    final_line = [newline1, newline2, newline3]
#
#    output_lines = []
#
#    if show_answers==False:
#        for i in range(len(final_line)-1):
#            line = ''
#            for n in final_line[i]:
#               line += n.rjust(8)
#            output_lines.append(line)
#    else:
#        for i in range(len(final_line)+1):
#            line = ''
#            for n in final_line[i]:
#                if i==2:
#                    line+='------'.rjust(8)
#                else:
#                    line += n.rjust(8)
#            output_lines.append(line)

        

#    for i in range(len(final_line)):
#        line = ''
#        for n in final_line[i]:
#            line += n.rjust(8)
#        output_lines.append(line)
              

#    return '\n'.join(output_lines)

#def addition(word):
#    sum = int(word[0]) + int(word[1])
#    return sum

#def subtraction(word2):
#    num1 = int(word2[0])
#    num2 = int(word2[1])
#    difference = num1 - num2
#    return difference

def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error. Too many problems"

    line1 = []
    line2 = []
    line3 = []

    first = ''
    second = ''
    lines = ''

    
    for part in problems:
        problem = part.split()
        operand1, operator, operand2 = problem
        sum = ""
        if operator == "+":
            sum = str(int(operand1) + int(operand2))
#            word = part.split('+')
#            sum = addition(word)
#            line1.append(int(word[0]))
#            line2.append(int(word[1]))
#            line3.append(sum)
        elif operator == "-":
            sum = str(int(operand1) - int(operand2))
#            word2 = part.split('-')
#            difference = subtraction(word2)
#            line1.append(int(word2[0]))
#            line2.append(int(word2[1]))
#            line3.append(difference)
        elif (re.search("[^\s0-9.+-", part)):
            return "Error: Numbers must only contain digits"
        elif (re.search("[/]", part) or re.search("[*]", part)):
            return "Error: Operator must be '+' or '-'"
        elif (len(operand1)>=5 or len(operand2)>=5):
            return "Error: Numbers cannot be more than 4 digits"
#        elif not operator1.isdigit() or not operator2.isdigit():
#            return "Error: Numbers must only contain digits."
#        elif len(operator1)>4 or len(operator2)>4:
#            return "Error: Numbers cannot be more than four digits."
#        elif operand not in ['+','-']:
#            return "Error: Operator must be '+' or '-'"
        else:
            return "Error"
        

    return print_lines(line1, line2, line3, show_answers)

            
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))