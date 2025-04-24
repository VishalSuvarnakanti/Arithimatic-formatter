def arithmetic_arranger(problems, show_answers=False):

    if len(problems)>5:
        return "Error. Too many problems"

    num3 = []

    for i in problems:
        num2 = []
        for n in i:
            num = []
            if n.isdigit():
                num.append(int(n))
            else:
                continue
            num2.append(num)
        num3.append(num2)

    return num3
    
    

sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)

