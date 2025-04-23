def arithmetic_arranger(problems, show_answers=False):

    num3 = []

    for i in problems:
        num2 = []
        for n in i:
            num = []
            if n.isdigit():
                num.append(n)
            else:
                continue
            run = ''.join(num)
            run2 = int(run)
            num2.append(run2)
        num3.append(num2)

    return num3
    
    

sum = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(sum)

