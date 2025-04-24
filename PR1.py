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
        if '+' in part:
            word = part.split('+')
            sum = addition(word)
            line1.append(sum)
        else:
            word2 = part.split('-')
            difference = subtraction(word2)
            line1.append(difference)
            
    return line1
    
sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)


