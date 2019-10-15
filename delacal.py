# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Enrique
#
# Created:     07/10/2019
# Copyright:   (c) Enrique 2019
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


def enri_ex1_params():
    actualParam = round(random.random() * 100, 3)
    return actualParam


def enri_ex1():
    param = enri_ex1_params()

    expectedanswer = '\'' + str(param) + '\'' + ' ' + str(float(param)) + ' ' + str(int(param))

    msg = {'EN_US': """You must type each result separated by ONE BLANK (quotes ' included if they are necessary)
                    What gets printed after executing the following piece of code?')
                    (Type "exit" (without quotes) to exit the program)
                    >>> str(%s)
                    >>> float(%s)
                    >>> int(%s)""" % (param, param, param)
        , 'ES_ES': """Debe teclear cada resultado separado del siguiente por un espacio en blanco (incluir comillas '' si es necesario
                    Indique que valores se imprimirán trás la ejecución del siguiente código?')
                    (Escriba "exit" (sin comillas) para salir del programa)
                    >>> str(%s)
                    >>> float(%s)
                    >>> int(%s)""" % (param, param, param)
           }[common.LANG]
    print(msg)
    answer = input()

    if answer.lower() == 'exit':
        return -2

    if (answer == expectedanswer):
        return 1
    else:
        return -1


# Inicia las variabbles global y local para ejecutar código.
def exec_sec_code_init():
    myCode = ""
    total = create_secure_dict()
    loc = initialize_local_dict()

    try:
        byte_code = compile_restricted(
            myCode,
            filename='<inline code>',
            mode='exec'
        )
        exec(byte_code, {'__builtins__': total}, loc)
    except SyntaxError as e:
        print(e)
    return [total, loc]


# Añade una variable al ambito local
def exec_sec_vars(total, loc, var_init):
    myCode = var_init
    try:
        byte_code = compile_restricted(
            myCode,
            filename='<inline code>',
            mode='exec'
        )
        exec(byte_code, {'__builtins__': total}, loc)
    except SyntaxError as e:
        print(e)
    return [total, loc]


# Ejecuta expresion line
def exec_sec_code(total, loc, line):
    myCode = "answer = %s" % (line);

    try:
        byte_code = compile_restricted(
            myCode,
            filename='<inline code>',
            mode='exec'
        )
        exec(byte_code, {'__builtins__': total}, loc)
    except SyntaxError as e:
        print(e)
    return loc['answer']


# Por terminar
def enri_ex2_params():
    param = [round(random.random() * 100, 3)]
    param += [21.0]
    return param


# answer: round((price*(vat+100))/100,2)
def enri_ex2():
    param = enri_ex2_params()

    expectedanswer = round((param[0] * (100 + param[1])) / 100.0, 2)
    [globals, locals] = exec_sec_code_init()
    [globals, locals] = exec_sec_vars(globals, locals, "expectedanswer = %f" % (expectedanswer))
    [globals, locals] = exec_sec_vars(globals, locals, "answer = 0")
    [globals, locals] = exec_sec_vars(globals, locals, "price = %f" % (param[0]))
    [globals, locals] = exec_sec_vars(globals, locals, "vat = %d" % (param[1]))
    globals['round'] = round;

    msg = {'EN_US': """Write the python expression to compute the final price (vat included) for an article with precision of 2 decimals
        Consider defined the variables: price and vat (in 100\%).
        (Type "exit" (without quotes) to exit the program)""",
           'ES_ES': """Escriba una expresión python que calcule el precio final (IVA incluído) para un artículo con precisión de 2 decimales
       Considere definidas las variables: price y vat (en 100\%)].
       (Escriba "exit" (sin comillas) para salir del programa)"""}[common.LANG]

    print(msg)
    line = input('>>> ')
    try:
        correct = type(exec_sec_code(globals, locals, line)) is float
    except:
        correct = False
    while not (correct or line == 'exit'):
        print(msg)
        line = input('>>> ')
        try:
            correct = type(exec_sec_code(globals, locals, line)) is float
        except:
            correct = False

    if (line == 'exit'):
        return -2

    answer = exec_sec_code(globals, locals, line)
    if (answer == expectedanswer):
        return 1
    else:
        return -1


def enri_ex3_params():
    params = [random.randint(1, 10)]
    params += [random.randint(1, 4)]
    params += [random.randint(1, 5)]
    return params


#answer: la respuesta es el resultado que tenga un desvío.
def enri_ex3():
    params = enri_ex3_params();
    x = params[0]
    y = params[1]
    bias = params[2]
    random.seed(a=None, version=2)
    result = random.randint(1, 4)

    msg = {'EN_US': """Given the variables x = %d and y = %d, 'Which of the following expression has NOT a right value?')
            (Type "exit" (without quotes) to exit the program)""" % (x, y),
           'ES_ES': """Dadas las variables x = %d y y = %d, '¿Cual de las siguientes expresiones no presenta un valor correcto?')
            (Escriba "exit" (sin comillas) para salir del programa)""" % (x, y)}[common.LANG]

    res = [x ** y]
    res += [x / y]
    res += [x * y]
    res += [x % y]
    res[result - 1] -= bias
    print(msg)
    print(' - 1. x**y = ', res[0])
    print(' - 2. x/y = ', res[1])
    print(' - 3. x*y = ', res[2])
    print(' - 4. x%y = ', res[3])
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


def enri_ex4_params():
    params = [random.randint(10, 20)]
    params += [2.33]
    return params


# Operadores //
def enri_ex4():
    params = enri_ex4_params()
    x = params[0]
    y = params[1]
    random.seed(a=None, version=2)
    result = random.randint(1, 4)

    msg = {'EN_US': """Given the variables x = %d and y = %d, 'Which of the following expression has NOT a right value?')
                (Type "exit" (without quotes) to exit the program)""" % (x, y),
           'ES_ES': """Dadas las variables x = %d y y = %d, '¿Cual de las siguientes expresiones no presenta un valor correcto?')
                (Escriba "exit" (sin comillas) para salir del programa)""" % (x, y)}[common.LANG]

    if (result == 1):
        res = [x // y]
    else:
        res = [x / y]
    if (result == 2):
        res = res + [x / y]
    else:
        res = res + [x // y]
    if (result == 3):
        res = res + [y // x]
    else:
        res = res + [y / x]
    if (result == 4):
        res = res + [y / x]
    else:
        res += [y // x]

    print(msg)
    print(' - 1. x/y = ', res[0])
    print(' - 2. x//y = ', res[1])
    print(' - 3. y/x = ', res[2])
    print(' - 4. y//x = ', res[3])
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


def enri_ex5_params():
    params = [random.randint(2, 5)]
    params += [random.randint(2, 5)]
    params += [random.randint(2, 5)]
    return params


# precedence
def enri_ex5():
    params = enri_ex5_params()
    x = params[0]
    y = params[1]
    z = params[2]
    result = random.randint(1, 4)
    res = [x - y * z ** 2]  # This is the right
    res += [x - (y * z) ** 2]
    res += [(x - y) * z ** 2]
    res += [(x - y * z) ** 2]
    numericanswer = res[result - 1]
    if (result == 1):
        expectedanswer = 'Yes'
    else:
        expectedanswer = 'No'
    msg = {'EN_US': """Given this expression x - y * z ** 2, Is the ANSWER = %f, 
        the RIGHT output considering the values x = %f, y = %f and z = %f.
        Type Yes or No
        (Type "exit" (without quotes) to exit the program)""" % (numericanswer, x, y, z),
           'ES_ES': """Dadas la expresión x - y * z ** 2, Es el valor = %f,
            el cálculo correcto para los valores  x = %f, y = %f and z = %f.
        Escriba como respuesta Yes o No
        (Escriba "exit" (sin comillas) para salir del programa)""" % (numericanswer, x, y, z)}[common.LANG]

    print(msg)
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


# '1 () 2 ** 3 +x -x ~x 4 * / // % 5 + - '
def enri_ex6_params():
    params = ['+ -x * ** ()']
    params += ['-x * () ** +']
    params += ['+ -x * ** ()']
    params += ['() + ** -x *']
    params += ['** + -x * ()']
    params += ['() ** -x * +']  # <-- this is the right answer
    return params


# 6 asociatividad.
def enri_ex6():
    params = enri_ex6_params()
    options = (list)(range(0, len(params)))
    random.shuffle(options)
    expectedanswer = str(options.index(5) + 1)

    msg = {'EN_US': """Given the following lists of operators, type the right option where the operators 
            are ordered by precedence (higher to lower)
           (Type "exit" (without quotes) to exit the program)""",
           'ES_ES': """Dadas las siguientes listas de operadores, escriba la opción correcta donde los operadores
            estén ordenados por precedencia (de mayor a menor)
           (Escriba "exit" (sin comillas) para salir del programa)"""}[common.LANG]

    print(msg)
    for i in range(len(params)):
        print(str(i + 1) + ') ' + params[options[i]])

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
def enri_ex7_params():
    params = ['2 ** 3 ** 2']
    params += ['(2 ** 3) ** 2']
    params += ['2 * 3 * 2']
    params += ['2 ** (3 * 2)']
    params += [2 ** 3 ** 2]
    params += [(2 ** 3) ** 2]
    params += [2 * 3 * 2]
    params += [2 ** (3 * 2)]

    return params


# 7 asociatividad
def enri_ex7():
    params = enri_ex7_params()
    expectedanswer = str(params[4])
    for i in range(5, 8):
        expectedanswer = expectedanswer + " " + str(params[i])

    msg = {'EN_US': """Given the following list of expressions,
               type the output for each one separated by a BLANK
              (Type "exit" (without quotes) to exit the program)
              ))""",
           'ES_ES': """Dadas la siguiente lista de expresiones, 
               escriba la salida de cada una separadas por un blanco
              (Escriba "exit" (sin comillas) para salir del programa)
              ))"""}[common.LANG]

    print(msg)
    for i in range(0, 4):
        print(str(i) + ') ' + params[i])

    result = input('>>> ')

    if (result == 'exit'):
        return -2

    if result == expectedanswer:
        return 1
    else:
        return -1


# Calcular la longitud de un número
def enri_ex8_params():
    param = [random.randint(100, 100000)]
    return param


def enri_ex8():
    param = enri_ex8_params()

    expectedanswer = len(str(param[0]))
    [globals, locals] = exec_sec_code_init()
    [globals, locals] = exec_sec_vars(globals, locals, "expectedanswer = %d" % (expectedanswer))
    [globals, locals] = exec_sec_vars(globals, locals, "answer = 0")
    [globals, locals] = exec_sec_vars(globals, locals, "number = %d" % (param[0]))
    globals['len'] = len;
    globals['str'] = str;

    msg = {'EN_US': """Write the python expression to compute the number of digits of a positive integer value (without sign).
            Consider defined the integer variable: number [100-100000].
            (Type "exit" (without quotes) to exit the program)""",
           'ES_ES': """Escriba una expresión python que calcule el número de digitos de un número entero positivo (sin signo).
           Considere definida la variable entera: number [100-100000].
           (Escriba "exit" (sin comillas) para salir del programa)"""}[common.LANG]

    print(msg)
    line = input('>>>')
    try:
        correct = type(exec_sec_code(globals, locals, line)) is int
    except:
        correct = False
    while not (correct or line == 'exit'):
        print(msg)
        answer = input('>>>')
        try:
            correct = type(exec_sec_code(globals, locals, line)) is int
        except:
            correct = False

    if (line == 'exit'):
        return -2

    answer = exec_sec_code(globals, locals, line)
    if (answer == expectedanswer):
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


def ex9_enri():
    param = ex9_enri_params()


    locals = {'v1': param[0], 'v2': param[1], 'v3': param[2], 'temp': 0}
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

    if (param[0] < param[1] and param[1] < param[2]):
        return 1
    else:
        return -1


# Logica/If-Else
# Select the right condition
def ex10_enri_params():
    param = [random.randint(1, 10)]  # v1
    param += [random.randint(1, 10)]  # v2
    param += [random.randint(1, 10)]  # v3
    param += [random.randint(1, 10)]  # p1
    param += [random.randint(1, 10)]  # p2
    param += [random.randint(1, 10)]  # p3
    return param


def ex10_enri(resuelto):
    param = ex9_enri_params()
    if (resuelto):
        return -3

    expectedanswer = not (param[0] > param[3] or param[1] < param[4] and param[2] == param[5])

    print('Type the result (True or False) of the evaluation of this logical expression:')
    print('not (v1 >' + str(param[3]) + ' or v2 < ' + str(param[4]) + ' and v3 == ' + str(param[5]))
    print('considering the values for v1 = ' + str(param[0]) + ', v2 = ' + str(param[1]) + 'and v3 = ' + str(param[2]))
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
