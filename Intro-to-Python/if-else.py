# learning about control statements in python using if-else 
# we also used some of the concept we learnt before like variables,basic math operation and print statement

myNum = 51
myOption = 'no'

if myNum > 50 :
    print('Greater than 50')
elif myNum < 30:
    print('less than 30')   
else:
    print(f'number is {myNum}')   


if(myOption == 'yes' or myOption == 'Yes'):
    print('pass')
else:
    print('no')  


# classwork

print('Welcome to even-odd finder \n')
num = int(input('Enter a number: '))

if num % 2 == 1 :
    print('odd')
else:
    print('even')    