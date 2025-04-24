def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error. Too many problems"
    
    line1 = []
    
    for part in problems:
        if '+' in part:
            word = part.split('+')
        else:
            word = part.split('-')
        
        line1.append(word)
    
    return line1
    

sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)


