# Mohamed Lamin Walon-Jalloh 50706
# Assignment 2
# Creating a custom truthtable from any given boolean expression

def truthTable():
    expression = input('Enter an boolean expression: \n')
    for i in expression:
        pass
    expression = expression.replace("+", " or ").replace("*" , " and ")
    print(expression)
    print('\n')
    print(f'The truthtable for the expression {expression}')
    print('------------------')
    print('A | B | C | Result')
    print('------------------')
    for A in [0,1]:
        for B in [0,1]:
            for C in [0,1]:
                result = expression.replace("A",str(A)).replace("B",str(B)).replace("C",str(C))
                # print(result) for checking purposes
                output = eval(result)
                print(f'{A} | {B} | {C} |  {int(output)}')

truthTable()

# checking = "A+B+C*D*E+B+C+A+B+D+C+E+E"
# mylist = []
# for i in checking:
#     if i != '+' and i != '*':
#         mylist.append(i)

# print(mylist) 
# mylist.sort()
# print(mylist)
# mylist = list(set(mylist))
# mylist.sort()
# print(mylist)
# print(len(mylist))      