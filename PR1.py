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
    
    for part in problems:
        problem = part.split()
        operator1, operand, operator2 = problem
        if '+' in part:
            word = part.split('+')
            sum = addition(word)
            line1.append(sum)
        elif '-' in part:
            word2 = part.split('-')
            difference = subtraction(word2)
            line1.append(difference)
        elif not operator1.isdigit() or not operator2.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(operator1)>4 or len(operator2)>4:
            return "Error: Numbers cannot be more than four digits."
        elif operand not in ['+','-']:
            return "Error: Operator must be '+' or '-'"
        else:
            return "Error"

    return line1

            

    
sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)


