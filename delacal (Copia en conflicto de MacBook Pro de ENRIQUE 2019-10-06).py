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
import common

from RestrictedPython import compile_restricted
from RestrictedPython.Eval import default_guarded_getiter
from RestrictedPython.Guards import guarded_iter_unpack_sequence
from RestrictedPython.Guards import safer_getattr

from RestrictedPython import safe_globals
from RestrictedPython import safe_builtins
from RestrictedPython import limited_builtins
from RestrictedPython import utility_builtins

from common import create_secure_dict
from common import initialize_local_dict
from common import safe_getitem_str
from common import add_getitem_str_to_local_dictionary


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
def enri_ex1():

    param = ex1_enri_params()

    result = '\'' + str(param) + '\'' + ' ' + str(float(param)) + ' ' + str(int(param))

    msg = {'EN_US':"""You must type each result separated by ONE BLANK (quotes ' included if they are necessary)
                    What gets printed after executing the following piece of code?')
                    (Type "exit" (without quotes) to exit the program)
                    >>> str(%s)
                    >>> float(%s)
                    >>> int(%s)"""%(param, param, param)
    , 'ES_ES':"""Debe teclear cada resultado separado del siguiente por un espacio en blanco (incluir comillas '' si es necesario
                    Indique que valores se imprimirán trás la ejecución del siguiente código?')
                    (Escriba "exit" (sin comillas) para salir del programa)
                    >>> str(%s)
                    >>> float(%s)
                    >>> int(%s)"""%(param, param, param)
           }[common.LANG]
    print(msg)
    line = input()

    if line.lower() == 'exit':
        return -2

    if (line == result):
        return 1
    else:
        return -1


def ex2_enri_params():
    param = [random.random()*100]
    param += [21.0]
    return param


def enri_ex2():
    param = ex2_enri_params()

    globals = {}
    locals = {'price' : param[0], 'vat' : param[1] }
    expectedanswer = round( (param[0]*(100+param[1]))/100.0, 2)

    msg = {'EN_US': """Write the python expression to compute the final price (vat included) for an article with precision of 2 decimals
        Consider defined the variables: price [10-100] and vat [0.0-100.0].
        (Type "exit" (without quotes) to exit the program)""",
       'ES_ES':"""Escriba una expresión python que calcule el precio final (IVA incluído) para un artículo con precisión de 2 decimales
       Considere definidas las variables: price [10-100] y vat [0.0-100.0].
       (Escriba "exit" (sin comillas) para salir del programa)"""}[common.LANG]

    print(msg)
    line = input('>>> ')
    try:
        correct = type(eval(line, globals, locals)) is float
    except:
        correct = False
    while not (correct or line == 'exit'):
        print(msg)
        line = input('>>> ')
        try:
            correct = type(eval(line, globals, locals)) is float
        except:
            correct = False

    if (line == 'exit'):
        return -2

    answer = eval(line, globals, locals)
    if (answer == expectedanswer):
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

    print('Given the variables x = ' + str(x) + ' and y =' + str(y) + 'Which of them is not right?')
    res = x ** y
    res += x / y
    res += x * y
    res += x % y
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
    res = x - y * z ** 2  # This is the right
    res += [x - (y * z) ** 2]
    res += [(x - y) * z ** 2]
    res += [(x - y * z) ** 2]
    numericanswer = res[result]
    if (result == 1):
        expectedanswer = 'Yes'
    else:
        expectedanswer = 'No'
    print('Given this expression x - y * z ** 2 , Is the ANSWER = ' + str(
        numericanswer) + ', the RIGHT output considering the values x = ' + str(x) + ', y =' + str(
        y) + ' and z = ' + str(z))
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


#'1 () 2 ** 3 +x -x ~x 4 * / // % 5 + - '
def ex6_enri_params():
    params = ['+ -x * ** ()']
    params += ['-x * () ** +']
    params += ['+ -x * ** ()']
    params += ['() + ** -x *']
    params += ['** + -x * ()']
    params += ['() ** -x * +'] #<-- this is the right answer
    return params

#6 precedence
def ex6_enri(resuelto):
    if (resuelto):
        return -3

    params = ex6_enri_params()
    options = (list)(range(0, len(params)))
    random.shuffle(options)
    expectedanswer = options.index(5)

    print(
    'Given the following lists of operators, type the right option where the operators are ordered by precedence (higher to lower)')

    for i in range(len(params)):
        print(str(i) + ') ' + params[options[i]])

    identifier = input('>>> ')

    if (identifier == 'exit'):
        return -2

    if (identifier not in ['1', '2', '3', '4', '5', '6']):
        print('Invalid option')
        return -1

    if identifier == expectedanswer:
       return 1
    else:
      return -1

# Vamos a trabajar con **, con * y
def ex7_enri_params():
    params = ['2 ** 3 ** 2']
    params += ['(2 ** 3) ** 2']
    params += ['2 * 3 * 2']
    params += ['2 * (3 * 2)']

    return params

#7 asociatividad
def ex7_enri():
    params = ex7_enri_params()
    expectedanswer = ''
    for i in range(len(params)):
        expectedanswer = expectedanswer + str(eval(params[i]))

    # print(str(i)+')'+params[i])
    for i in range(len(params)):
        print(str(i)+')'+params[i])

    print('Given the following lists of expressions, type the output for each one separated by a BLANK)')

    for i in range(len(params)):
        print(str(i) + ') ' + params[i])

    result = input('>>> ')

    if (result == 'exit'):
        return -2

    if result == expectedanswer:
        return 1
    else:
        return -1

  # Calcular la longitud de un número
def ex8_enri_params():
    param = [random.randint(100, 100000)]
    return param


def ex8_enri(resuelto):
    param = ex8_enri_params()
    if (resuelto):
        return -3

    locals = {'number' : param[0] }
    resul = len(str(param[0]))
    globals = {}
    print('Write the python expression to compute the number of digits of a positive value (without sign)')
    print('Consider defined the variable: numer [100-100000]')
    print('(Type "exit" (without quotes) to exit the program)')
    line = input('Number of digits: ')
    try:
        correct = type(eval(line, globals, locals)) is int
    except:
        correct = False
    while not (correct or line == 'exit'):
        print('Write the python expression to compute the number of digits of a positive value (without sign)')
        print('Consider defined the variable: numer [100-100000]')
        print('(Type "exit" (without quotes) to exit the program)')
        line = input('Number of digits: ')
        try:
            correct = type(eval(line, globals, locals)) is int
        except:
            correct = False

    if (line == 'exit'):
        return -2

    if (line == resul):
        return 1
    else:
        return -1


# Logica/If-Else
# Write the condicions in order to get the 3 variables v1, v2 and v3 ordered
def ex9_enri_params():
    param = [random.randint(20, 30)]
    param += [random.randint(10, 19)]
    param += [random.randint(1, 9)]
    return param


def ex9_enri(resuelto):
    param = ex9_enri_params()
    if (resuelto):
        return -3

    locals = {'v1' : param[0], 'v2' : param[1], 'v3' : param[2], 'temp' : 0}
    globals = {}
    print('Considering the following code:')
    print('\t if condition1:')
    print('\t\t temp = v2')
    print('\t\t v2 = v1')
    print('\t\t v1 = v2')
    print('\t if condition1:')
    print('\t\t temp = v3')
    print('\t\t v3 = v2')
    print('\t\t v2 = v3')
    print('Write the python logical conditions: condition1 and condition2 in order to get the 3 variables v1, v2 and v3 ordered')
    print('Consider defined the variables: v1, v2, v3 and temp')
    print('(Type "exit" (without quotes) to exit the program)')
    line1 = input('condition1: ')
    if (line1 == 'exit'):
        return -2
    line2 = input('condition2: ')
    if (line2 == 'exit'):
        return -2
    try:
        correct1 = type(eval(line1, globals, locals)) is bool
        correct2 = type(eval(line2, globals, locals)) is bool
        correct = correct1 and correct2
    except:
        correct = False
    while not (correct or line1 == 'exit'):
        print('Considering the following code:')
        print('\t if condition1:')
        print('\t\t temp = v2')
        print('\t\t v2 = v1')
        print('\t\t v1 = v2')
        print('\t if condition1:')
        print('\t\t temp = v3')
        print('\t\t v3 = v2')
        print('\t\t v2 = v3')
        print(
            'Write the python logical conditions: condition1 and condition2 in order to get the 3 variables v1, v2 and v3 ordered')
        print('Consider defined the variables: v1, v2, v3 and temp')
        print('(Type "exit" (without quotes) to exit the program)')
        line1 = input('condition1: ')
        if (line1 == 'exit'):
            return -2
        line2 = input('condition2: ')
        if (line2 == 'exit'):
            return -2
        try:
            correct1 = type(eval(line1, globals, locals)) is bool
            correct2 = type(eval(line2, globals, locals)) is bool
            correct = correct1 and correct2
        except:
            correct = False

    if (eval(line1, globals, locals)):
        temp = param[1]
        param[1] = temp
        param[0] = param[1]

    if (eval(line2, globals, locals)):
        temp = param[2]
        param[2] = temp
        param[1] = param[2]

    if (param[0]<param[1] and param[1]<param[2]):
        return 1
    else:
        return -1

# Logica/If-Else
# Select the right condition
def ex10_enri_params():
    param = [random.randint(1, 10)]  #v1
    param += [random.randint(1, 10)] #v2
    param += [random.randint(1, 10)] #v3
    param += [random.randint(1, 10)] #p1
    param += [random.randint(1, 10)] #p2
    param += [random.randint(1, 10)] #p3
    return param

def ex10_enri(resuelto):
    param = ex9_enri_params()
    if (resuelto):
        return -3

    expectedanswer = not(param[0] > param[3]  or param[1] < param[4] and param[2] == param[5])

    print('Type the result (True or False) of the evaluation of this logical expression:')
    print('not (v1 >'+ str(param[3]) + ' or v2 < '+str(param[4])+ ' and v3 == '+str(param[5]))
    print('considering the values for v1 = '+str(param[0])+', v2 = '+str(param[1])+'and v3 = '+str(param[2]))
    identifier = input('>>> ')

    if (identifier == 'exit'):
        return -2

    if (identifier not in ['True', 'False']):
        print('Invalid option!')
    return -1

    if identifier == expectedanswer:
        return 1
    else:
        return -1
