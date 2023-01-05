# I tried to use the conditional structures that I have learned in Python

import math

num1 = float(input('Enter Num1: '))

ops = ['Log [1]', 'Fac [2]', 'Sqrt [3]', '+ [4]', '- [5]', '* [6]', '/ [7]', '** [8]']

print(ops)

inpOp = int(input('Enter Operator: '))

isAnotherNumberNeeded = True

if inpOp >= 1 and inpOp <= 3:
    isAnotherNumberNeeded = False

if isAnotherNumberNeeded == False:
    if inpOp == 1:
        print(math.log(num1))
    elif inpOp == 2:
        print(math.factorial(int(num1)))
    elif inpOp == 3:
        print(math.sqrt(num1))
else:
    if inpOp >= 4 and inpOp <= 8:
        num2 = float(input('Enter Num2: '))
        if inpOp == 4:
            print('Result: ', num1 + num2)
        elif inpOp == 5:
            print('Result: ', num1 - num2)
        elif inpOp == 6:
            print('Result: ', num1 * num2)
        elif inpOp == 7:
            if num2 == 0:
                print("Dev by Zero is not valid.")
            else:
                print('Result: ', num1 / num2)
        elif inpOp == 8:
            print(math.pow(num1, num2))
    else:
        print('Invalid Operator.')