"""
Date: Oct 31, 2018
Author: Beatriz Remeseiro

The exercises return one of the following values:
   -3: already solved
   -2: exit
   -1: incorrect solution
    1: correct solution
"""

import random

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Conversion of numbers from decimal to binary
def exB1_params():
    param = random.randint(0, 128)
    return param

def exB1(solved):
    if (solved):
        return -3

    param = exB1_params()
    result = bin(param)

    print('What is the result of executing the following sentence?')
    print('You must type the solution without quotes')
    print('(Type "exit" (without quotes) to exit the program)')
    print('>>> bin(' + str(param) + ')')

    line = input()
    if (line.lower()=='exit'):
        return -2
    elif (line==result):
        return 1
    else:
        return -1

# Output of an if-elif followed by another if
def exB2_params():
    param = random.randint(0, 10)
    return param

def exB2(solved):
    if (solved):
        return -3

    param = exB2_params()
    result = '> '
    if param > 7:
        result = result + 'a '
    elif param // 2 == 3:
        result = result + 'b '
    if (param + 2 > 6):
        result = result + 'c '

    print('What is the value of the variable "result" (without quotes) after executing the following code for x = %d?' % param)
    print('You must type the solution without quotes')
    print('(Type "exit" (without quotes) to exit the program)')
    print('\t result=\'> \'')
    print('\t if x>7:')
    print('\t\t result = result + \'a \'')
    print('\t elif x//2==3:')
    print('\t\t result = result + \'b \'')
    print('\t if x+2>6:')
    print('\t\t result = result + \'c \'')

    line = input()
    if (line.lower() == 'exit'):
        return -2
    elif (line == result):
        return 1
    else:
        return -1

# Output of a for loop that includes an if
def exB3_params():
    param = [random.randint(-10, 10)]
    param += [random.randint(-10, 10)]
    param += [random.choice([-2,-1,1,2])]
    return param

def exB3(solved):
    if (solved):
        return -3

    param = exB3_params()
    result = '> '
    for i in range(param[0], param[1], param[2]):
        if i % 2 == 0:
            result = result + str(i) + ' '
        else:
            result = result + str(i-1) + ' '

    print('What is the value of the variable "result" (without quotes) after executing the following code?')
    print('You must type the solution without quotes')
    print('(Type "exit" (without quotes) to exit the program)')
    print('\t result=\'> \'')
    print('\t for i in range(%d, %d ,%d):' % (param[0], param[1], param[2]))
    print('\t\t if i%2==0:')
    print('\t\t\t result = result + str(i) + \' \'')
    print('\t\t else:')
    print('\t\t\t result = result + str(i-1) + \' \'')

    line = input()
    if (line.lower() == 'exit'):
        return -2
    elif (line == result):
        return 1
    else:
        return -1

# Number of iterations of an inside loop (using two nested loops)
def exB4_params():
    param = [random.randint(-10, 10)]
    param += [random.randint(-10, 10)]
    param += [random.choice([-2,-1,1,2])]
    param += [random.randint(-10, 10)]
    param += [random.randint(-10, 10)]
    param += [random.choice([-2,-1,1,2])]
    return param

def exB4(solved):
    if (solved):
        return -3

    param = exB4_params()
    result = 0
    for i in range(param[0], param[1], param[2]):
        for i in range(param[3], param[4], param[5]):
            result = result+1

    print('How many iterations does the inside loop of the following code?')
    print('(Type "exit" (without quotes) to exit the program)')
    print('\t for i in range(%d, %d ,%d):' % (param[0], param[1], param[2]))
    print('\t\t for i in range(%d, %d ,%d):' % (param[3], param[4], param[5]))
    print('\t\t\t print(i*j)')

    line = input()
    while not (is_int(line) or line == 'exit'):
        print('\nYou must type an integer number')
        print('How many iterations does the inside loop of the following code?')
        print('(Type "exit" (without quotes) to exit the program)')
        print('\t for i in range(%d, %d ,%d):' % (param[0], param[1], param[2]))
        print('\t\t for i in range(%d, %d ,%d):' % (param[3], param[4], param[5]))
        print('\t\t\t print(i*j)')
        line = input()

    if (line.lower() == 'exit'):
        return -2
    elif (int(line) == result):
        return 1
    else:
        return -1


# Country code of a telephone number (working with strings)
def exB5_params():
    param = [random.randint(10, 99)]
    param += [random.randint(600000000, 699999999)]
    return param

def exB5(solved):
    if (solved):
        return -3

    param = exB5_params()
    telephone = '+' + str(param[0]) + " " + str(param[1])
    result1 = '\'' + telephone + '\'.split()'
    result2 = '\'' + telephone + '\'.split(" ")'
    result3 = '\'' + telephone + '\'.split(\' \')'

    print('Given the telephone number \'' + telephone + '\', replace the ellipsis in the following line of code')
    print('to have the country code in the variable "c" and the number in the variable "n" (whithout quotes):')
    print('\t c, n = ...')
    print('(Type "exit" (without quotes) to exit the program)')

    line = input('c, n = ')
    if (line.lower() == 'exit'):
        return -2
    elif (line == result1 or line == result2 or line == result3):
        return 1
    else:
        return -1


# From all the elements in a list, the last one in alphabetical order
def exB6(solved):
    if (solved):
        return -3

    print('Given a list of students\' names stored in the variable "list" (without quotes),')
    print('replace the ellipsis in the following line of code to print the last name in alphabetical order:')
    print('\t print(...)')
    print('Be careful to name the variable exactly as "list" (without quotes)!')
    print('(Type "exit" (without quotes) to exit the program)')

    line = input()
    line = line.replace(" ", "")
    if (line.lower() == 'exit'):
        return -2
    elif (line == 'sorted(list)[len(list)-1]' or line == 'sorted(list)[-1]'):
        return 1
    else:
        return -1

# List that returns a given function (the function receives a list of integer numbers and returns a list of booleans
# indicating if the numbers are odd (True) or not (False)
def exB7_params():
    number = random.randint(1, 5)
    param = [random.randint(1, 20)]
    for i in range(number):
        param += [random.randint(1, 20)]
    return param

def exB7(solved):
    if (solved):
        return -3

    param = exB7_params()
    result = param.copy()
    for i in range(len(result)):
        result[i] = result[i] % 2 == 1

    print('What does the following function return if it receives the list ' + str(param) + '?')
    print('\t def int_list(list):')
    print('\t\t for i in range(len(list)):')
    print('\t\t\t list[i] = list[i] % 2 == 1')
    print('\t\t return list')
    print('Use this format: [a, b, c, d, ...]')
    print('(Type "exit" (without quotes) to exit the program)')

    line = input()
    try:
        correct = type(eval(line)) is list
    except:
        correct = False

    while not (correct or line=='exit'):
        print('\nYou must type a list with this format: [a, b, c, d, ...]')
        print('What does the following function return if it receives the list ' + str(param) + '?')
        print('\t def new_list(list):')
        print('\t\t for i in range(len(list)):')
        print('\t\t\t list[i] = list[i] % 2 == 1')
        print('\t\t return list')
        print('(Type "exit" (without quotes) to exit the program)')
        line = input()
        try:
            correct = type(eval(line)) is list
        except:
            correct = False

    if (line=='exit'):
        return -2

    try:
        line = line.strip()
        if (line[0]!='[' or line[-1]!=']'):
            return -1
        line = eval(line)
    except:
        return -1

    if (line==result):
        return 1
    else:
        return -1

# Write a given name with the first letter in capital
def exB8_params():
    names = ['olivia', 'emma', 'charlotte', 'sophia', 'isabella', 'noah', 'benjamin', 'oliver', 'william', 'james']
    n = random.randint(0,len(names)-1)
    param = names[n]
    return param

def exB8(solved):
    if (solved):
        return -3

    param = exB8_params()
    name_capital = chr(ord(param[0]) - 32) + param[1:len(param)]
    result = 'chr(ord(\'' + param + '\'[0])-32)+\'' + param + '\'[1:len(\'' + param + '\')]'
    result2 = 'chr(ord(\'' + param + '\'[0])-32)+\'' + param + '\'[1:]'

    print('Given the name \'' + param + '\', replace the ellipsis in the following line of code')
    print('to have this name with the first letter in capital (i.e. \'%s\')' % name_capital)
    print('in the variable "name" (whithout quotes):')
    print('\t name = ...')
    print('Note that you have to use always exactly the given name \'' + param + '\' and not a part of it.')
    print('Use len(\'' + param + '\') if you need the number of letters of the name.')
    print('\nWARNING!')
    print('It is forbidden to use the methods upper() or lower() in this exercise.\n')
    print('(Type "exit" (without quotes) to exit the program)')

    line = input('name = ')
    line = line.replace(" ", "")
    if (line.lower() == 'exit'):
        return -2
    elif (line == result or line == result2):
        return 1
    else:
        return -1