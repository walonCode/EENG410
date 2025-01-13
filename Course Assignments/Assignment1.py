##  Assignment 1 
# To use python to solve momentum and kinetic energy

## Required values from the user
print('Welcome To Momentum and Kinetic Solver.......!!!!😊❤️ \n')

mass = float(input('Enter your mass value: '))
velocity = float(input('Enter you velocity value: '))

def momentum(mass, velocity):
    # since we know that momentum formula is mass multiply by velocity
    # we store  that answer in the answer variable

    answer = mass * velocity
    return answer

def kinetic(mass,velocity):
    #the formular for kinetic energy is 0.5 multiply by mass multiply by velocity squared
    # answer is store in an answer variable


    answer = 1/2 * ((mass) * (velocity ** 2))
    return answer

print(f'Your momentum is : {momentum(mass, velocity)} N/s')
print(f'Your kinetic energy is:  {kinetic(mass, velocity)} Joules ')