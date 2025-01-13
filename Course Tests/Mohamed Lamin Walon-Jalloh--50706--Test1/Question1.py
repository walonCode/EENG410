## Mohamed Lamin Walon-Jalloh --- 50706--
## Test

## Question 1

def generatetruthtable(bool_expression):
    print(f"\n Truth Table for Expression: {bool_expression}")
    print("=" * 21)
    print("| A | B | C | D | Y |")
    print("=" * 21)

    for A in [0, 1]:
        for B in [0, 1]:
            for C in [0, 1]:
                for D in [0, 1]:

                    temporaryExpression = bool_expression

                    while "'" in temporaryExpression:
                        compOsition = temporaryExpression.index("'")
                        compliment = temporaryExpression[compOsition - 1]
                        value = 1 - (A if compliment == 'A' else B if compliment == 'B' else C if compliment == 'C' else D)
                        temporaryExpression = temporaryExpression.replace(f"{compliment}'", str(value))

                    temporaryExpression = temporaryExpression.replace('A', str(A)).replace('B', str(B)).replace('C',str(C)).replace('D', str(D))

                    i = 0
                    while i < len(temporaryExpression) - 1:
                        if temporaryExpression[i].isdigit() and temporaryExpression[i + 1].isdigit():
                            temporaryResult = int(temporaryExpression[i]) & int(temporaryExpression[i + 1])
                            temporaryExpression = temporaryExpression[:i] + str(temporaryResult) + temporaryExpression[i + 2:]
                            i = 0
                        else:
                            i += 1

                    temporaryExpression = temporaryExpression.replace(' + ', ' or ')

                    output = eval(temporaryExpression)

                    print(f"| {A} | {B} | {C} | {D} | {output}")
    print("=" * 21)


## testing to seee if the function works
generatetruthtable("AB'+ CD")
generatetruthtable("ABC + BD")
generatetruthtable("A'B'D' + CD")
generatetruthtable("BC + A'D")
