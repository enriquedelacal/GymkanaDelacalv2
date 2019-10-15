# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Antonio
#
# Created:     30/05/2018
# Copyright:   (c) Antonio 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import random
import time
import re


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def ex1_enri_params():
    actualParam = round(random.random() * 100, 3)
    return actualParam


# Return:  
#     -3: Already solved
#     -2: Exit
#     -1: Incorrect sol.
#      1: Correct sol.
def ex1_enri(resuelto):
    if (resuelto):
        return -3
    param = ex1_enri_params()

    result = '\'' + str(param) + '\'' + ' ' + str(float(param)) + ' ' + str(int(param)) + '\''
    print('What gets printed after executing the following piece of code?')
    print('(Type "exit" (without quotes) to exit the program)')
    print('>>> ' + 'str( ' + param + ')')
    print('>>> ' + 'float( ' + param + ')')
    print('>>> ' + 'int( ' + param + ')')

    line = input()
    while not (check_int(line) or line == 'exit'):
        print('\nYou must type each result separated by ONE BLANK (quotes included if they are necessary)')
        print('What gets printed after executing the following piece of code?')
        print('(Type "exit" (without quotes) to exit the program)')
        print('>>> ' + 'str(' + param + ')')
        print('>>> ' + 'float(' + param + ')')
        print('>>> ' + 'int(' + param + ')')
        line = input()

    if line.lower() == 'exit':
        return -2

    line = int(line)

    if (line == result):
        return 1
    else:
        return -1


def ex2_enri_params():
    param = [random.random()*100]
    param += [0.21]
    return param


def ex2_enri(resuelto):
    param = ex2_enri_params()
    if (resuelto):
        return -3

    globals = {'price' : param[0], 'vat' : param[0] }
    resul = param[0]*(1+param[1])
    locals = {}
    print('Write the python expression to compute the final price (vat included) for an article with precision of 2 decimals?')
    print('Consider defined the variables: price [10-100] and vat [0-1]')
    print('(Type "exit" (without quotes) to exit the program)')
    line = input('Final price: ')
    try:
        correct = type(eval(line, globals, locals)) is float
    except:
        correct = False
    while not (correct or line == 'exit'):
        print('Write the python expression to compute the final price (vat included) for an article with precision of 2 decimals?')
        print('Consider defined the variables: price [10-100] and vat [0-1]')
        print('(Type "exit" (without quotes) to exit the program)')
        line = input('Final price: ')
        try:
            correct = type(eval(line, globals, locals)) is float
        except:
            correct = False

    if (line == 'exit'):
        return -2

    if (line == resul):
        return 1
    else:
        return -1


def ex3_enri_params():
     params = [random.randint(1, 10)]
     params += [random.randint(1, 4)]
     params += [random.randint(1, 5)]
     return params

def ex3_enri(resuelto):

        if (resuelto):
            return -3
        params = ex3_enri_params();
        x = params[0]
        y = params[1]
        bias = params[2]
        result = random.randint(1, 4)

        print('Given the variables x = '+ str(x) + ' and y =' + str(y) + 'Which of them is not right?')
        res = x**y
        res += x/y
        res += x*y
        res += x%y
        res[result] -= bias

        print(' - 1. x**y = ', res[0])
        print(' - 2. x/y = ', res[1])
        print(' - 3. x*y = ', res[2])
        print(' - 4. x%y = ', res[3])
        print('(Type "exit" (without quotes) to exit the program)')
        identifier = input('>>> ')

        if (identifier == 'exit'):
            return -2

        if (identifier not in ['1', '2', '3', '4']):
            print('Invalid option!')
            return -1

        if identifier == str(result):
            return 1
        else:
            return -1


def ex4_enri_params():
    params = [random.randint(10, 20)]
    params += [2.33]
    return params
# Operadores //
def ex4_enri(resuelto):
    if (resuelto):
        return -3
    params = ex4_enri_params()
    x = params[0]
    y = params[1]
    result = random.randint(1, 4)

    print('Given the variables x = ' + str(x) + ' and y =' + str(y) + 'Which of the following expressions is not right?')
    if (result == 1):
        res = x//y
    else:
        res = x/y
    if (result == 2):
        res += [x/y]
    else:
        res += [x//y]
    if (result == 3):
        res += [y//x]
    else:
        res += [y/x]
    if (result == 4):
        res += [y/x]
    else:
        res += [y//x]

    print(' - 1. x/y = ', res[0])
    print(' - 2. x//y = ', res[1])
    print(' - 3. y/x = ', res[2])
    print(' - 4. y//x = ', res[3])
    print('(Type "exit" (without quotes) to exit the program)')
    identifier = input('>>> ')

    if (identifier == 'exit'):
        return -2

    if (identifier not in ['1', '2', '3', '4']):
        print('Invalid option!')
        return -1

    if identifier == str(result):
        return 1
    else:
        return -1

def ex5_enri_params():
    params = [random.randint(2, 5)]
    params += [random.randint(2, 5)]
    params += [random.randint(2, 5)]
    return params

#precedence
def ex5_enri(resuelto):
  if (resuelto):
            return -3
        params = ex5_enri_params()
        x = params[0]
        y = params[1]
        z = params[2]
        result = random.randint(1, 4)
        res = x - y * z ** 2 # This is the right
        res += [x - (y * z) ** 2]
        res += [(x - y) * z ** 2]
        res += [(x - y * z) ** 2]
        numericanswer = res[result]
        if (result == 1):
            expectedanswer = 'Yes'
        else:
            expectedanswer = 'No'
        print('Given this expression x - y * z ** 2 , Is the ANSWER = '+str(numericanswer)+ ', the RIGHT output considering the values x = '+ str(x) + ', y =' + str(y) + ' and z = ' + str(z))
        print('Type Yes or No')
        print('(Type "exit" (without quotes) to exit the program)')
        identifier = input('>>> ')

        if (identifier == 'exit'):
            return -2

        if (identifier not in ['Yes', 'No']):
            print('Invalid option!')
            return -1

        if identifier == expectedanswer:
            return 1
        else:
            return -1


#'1 () 2 ** 3 +x -x ~x 4 * / // % 5 + - 6 << >> & ^ |'
def ex6_enri_params():
    params = ['+ -x * ** ()']
    params += ['-x * () ** +']
    params += ['+ -x * ** ()']
    params += ['() + ** -x *']
    params += ['** + -x * ()']
    params += ['() ** -x * +'] #this is the right answer
    return params

#6 procedence
def ex6_enri(resuelto):
  if (resuelto):
      return -3

   params = ex6_enri_params()
  random.shuffle(params)
  rightanswer = 5

    n = paramsresult = random.randint(1, 4)
    res = x ** y ** z ** 2 # This is the right,
    res += [(x ** y) ** z ** 2]
        res += [(x ** y ** z) ** 2]
        res += [x ** (y ** z) ** 2]
        numericanswer = res[result]
        if (result == 1):
            expectedanswer = 'Yes'
        else:
            expectedanswer = 'No'
        print('Given the following lists of operators, type the right option where the operators are ordered by precedence')
        identifier = input('>>> ')

        if (identifier == 'exit'):
            return -2

        if (identifier not in ['1', '2', '3' , '4', '5', '6']):
            print('Invalid option!')
            return -1

        if identifier == expectedanswer:
            return 1
        else:
            return -1

#x INtercambiar el primer caracter de dos cadenas (eval). (Pendiente)
