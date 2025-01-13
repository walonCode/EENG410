# Mohamed Lamin Walon-Jalloh 50706
# Test

## Question 2


#the resistor tuple
resistorTuple = (470,1200,330,2200,120,100)

##a
R1,R2,R3,R4,R5,R6 = resistorTuple
print(R1,R2) 

##b
def calculateResistorsInParallel (R1,R2,R5):
    parallelResistance = ((1/R1)+(1/R2)+(1/R5)) ** -1
    return parallelResistance

# testing the function
answer  = calculateResistorsInParallel(R1,R2,R5)
print(answer)

##c
resistorsBelow1000 = []
for i in resistorTuple:
    if i < 1000:
        resistorsBelow1000.append(i)

print(resistorsBelow1000)

##d
def calculateResistorInSeries(arr):
    seriesResistance = 0
    for i in arr:
        seriesResistance += i

    return seriesResistance

value = calculateResistorInSeries(resistorsBelow1000)
print(value)

##e
resistorsBelow1000.sort()
print(resistorsBelow1000)    
