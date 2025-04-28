def print_lines(line1, line2, line3):
    newline1 = [str(i) for i in line1]
    newline2 = [str(i) for i in line2]
    newline3 = [str(i) for i in line3]
    final_line = []
    final_line.append(newline1)
    final_line.append(newline2)
    final_line.append(newline3)

    for i in range(len(final_line)):
        for n in final_line[i]:
            print(n.rjust(6), end='')
        print(end='\n')


#           print(*final_line[i] , end='\n')

def addition(word):
    sum = int(word[0]) + int(word[1])
    return sum

def subtraction(word2):
    num1 = int(word2[0])
    num2 = int(word2[1])
    difference = num1 - num2
    return difference

def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error. Too many problems"

    line1 = []
    line2 = []
    line3 = []
    
    for part in problems:
        problem = part.split()
        operator1, operand, operator2 = problem
        if '+' in part:
            word = part.split('+')
            sum = addition(word)
            line1.append(int(word[0]))
            line2.append(int(word[1]))
            line3.append(sum)
        elif '-' in part:
            word2 = part.split('-')
            difference = subtraction(word2)
            line1.append(int(word2[0]))
            line2.append(int(word2[1]))
            line3.append(difference)
        elif not operator1.isdigit() or not operator2.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(operator1)>4 or len(operator2)>4:
            return "Error: Numbers cannot be more than four digits."
        elif operand not in ['+','-']:
            return "Error: Operator must be '+' or '-'"
        else:
            return "Error"
        
        
    return print_lines(line1, line2, line3)

            
sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)