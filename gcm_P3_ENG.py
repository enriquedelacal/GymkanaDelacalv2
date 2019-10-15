# -*- coding: utf-8 -*-
"""
@author: Gabriel Cebrián Márquez (cebriangabriel@uniovi.es)
"""
import random

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isbool(s):
    try: 
        bool(s)
        return s == 'True' or s == 'False'
    except ValueError:
        return False

#1.- precedencia de operadores aritméticos, lógicos y relacionales.
def gcm_ex1_params():
    operands = list()
    operands.append(random.randint(1, 9))
    operands.append(random.randint(1, 4) * 2)
    operands.append(random.randint(1, 2) * 2)
    operands.append(random.randint(-9, 9))
    operands.append(random.randint(1, 9))
    operands.append(random.randint(1, 4) * 2)
    operands.append(random.randint(1, 2) * 2)
    operands.append(random.randint(-9, 9))

    operators = list()
    operators.append(random.choice('+-'))
    operators.append(random.choice('*/'))
    operators.append(random.choice(['<', '<=', '>', '>=']))
    operators.append(random.choice(['and', 'or']))
    operators.append(random.choice('+-'))
    operators.append(random.choice('*/'))
    operators.append(random.choice(['<', '<=', '>', '>=']))

    params = dict()
    params['operands'] = operands
    params['operators'] = operators
    
    return params

def gcm_ex1(solved):
    params = gcm_ex1_params()

    if solved:
        return -3

    expression = '{0} {8} {1} {9} {2} {10} {3} {11} {4} {12} {5} {13} {6} {14} {7}'.format(*(params['operands'] + params['operators']))
    msg = """What is the result of the following expression?
(Type "exit" (without quotes) to exit the program)
>>> {0}
""".format(expression)

    print(msg)
    answer = input("Answer: ")

    result = eval('{0}'.format(expression))

    if answer == 'exit':
        return -2
    elif answer == str(result):
        return 1
    else:
        return -1

#2.- especificar un valor cualquiera que ha de tener una variable para que se cumpla la condición de un if.
def gcm_ex2_params():
    operands = list()
    operands.append(random.randint(2, 5))
    operands.append(random.randint(2, 6))
    operands.append(random.randint(2, 6))
    operands.append(random.randint(1, 2) * 2)

    a = random.randint(-7, 7)
    limit = operands[0] * a - operands[1] * operands[2] // operands[3]
    operands.append(limit)

    params = dict()
    params['operands'] = operands
    
    return params

def gcm_ex2(solved):
    params = gcm_ex2_params()

    if solved:
        return -3

    expression = '{0} * {{0}} - {1} * {2} // {3} > {4}'.format(*params['operands'])
    msg = """Specify a valid integer value to which 'a' should be set so that the following code shows 'Option 2' on screen after its execution.
(Type "exit" (without quotes) to exit the program)

if {0}:
    print('Option 1')
else:
    print('Option 2')
""".format(expression.format('a'))

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    result = eval(expression.format(answer))

    if not result:
        return 1
    else:
        return -1

#3.- dado un fragmento de código con un if-elif-else, indicar qué imprimiría tras su ejecución (determinar qué ramal toma).
def gcm_ex3_params():
    operands = list()
    operands.append(random.randint(5, 15))
    operands.append(operands[0] + random.randint(3, 9))
    operands.append(operands[1] + random.randint(3, 9))
    operands.append(operands[2] + random.randint(3, 9))
    operands.insert(0, random.choice(list(range(operands[0] - 4 - operands[0] % 2, operands[0])) + list(range(operands[1], operands[2]))))

    params = dict()
    params['operands'] = operands

    return params

def gcm_ex3(solved):
    params = gcm_ex3_params()

    if solved:
        return -3

    msg = """Specify which value would be shown on screen after the execution of the following code. For instance, if print(15) is executed, then your answer should be "15" (without quotes).
(Type "exit" (without quotes) to exit the program)

n = {0}
if n < {1} and n % 2 != 0:
    print(1)
elif n < {2}:
    print(2)
elif n < {3} and n % 2 == 0:
    print(3)
elif n < {4}:
    print(4)
else:
    print(5)
""".format(*params['operands'])

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    n = params['operands'][0]
    if n < params['operands'][1] and n % 2 != 0:
        if answer == '1':
            return 1
        else:
            return -1
    elif n < params['operands'][2]:
        if answer == '2':
            return 1
        else:
            return -1
    elif n < params['operands'][3] and n % 2 == 0:
        if answer == '3':
            return 1
        else:
            return -1
    elif n < params['operands'][4]:
        if answer == '4':
            return 1
        else:
            return -1
    else:
        if answer == '5':
            return 1
        else:
            return -1

#4.- indicar nº veces que se ejecuta print (o similar) dentro de un bucle while (dificultad baja).
def gcm_ex4_params():
    operands = list()
    operands.append(random.randint(50, 80))
    operands.append(random.randint(2, 5) * 2 - 1)
    operands.append(random.randint(3, 8))
    operands.append(random.randint(1, 3) * 10)

    params = dict()
    params['operands'] = operands

    return params

def gcm_ex4(solved):
    params = gcm_ex4_params()

    if solved:
        return -3

    msg = """Specify which value would be stored in the variable 'counter' after the execution of the following program.
(Type "exit" (without quotes) to exit the program)

n = {0}
counter = 0
while n >= 0:
    n = n - {1}
    counter = counter + {2}
counter = counter + {3}
""".format(*params['operands'])

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    n = params['operands'][0]
    counter = 0
    while n >= 0:
        n = n - params['operands'][1]
        counter = counter + params['operands'][2]

        if counter > 10000: # Just in case... although it should not happen.
            return -2
    counter = counter + params['operands'][3]

    if counter == int(answer):
        return 1
    else:
        return -1

#5.- indicar nº veces que se ejecuta print (o similar) dentro de un bucle while (dificultad más elevada).
def gcm_ex5_params():
    operands = list()
    operands.append(random.randint(40, 60))
    operands.append(random.randint(-40, -20))
    operands.append(random.randint(2, 5) * 2 - 1)

    params = dict()
    params['operands'] = operands

    return params

def gcm_ex5(solved):
    params = gcm_ex5_params()

    if solved:
        return -3

    msg = """Specify which value would be stored in the variable 'counter' after the execution of the following program.
(Type "exit" (without quotes) to exit the program)

n = {0}
counter = 0
while n > {1}:
    if n > 0 and n % 2 == 0:
        n = n // 2
    else:
        n = n - {2}
    counter = counter + 1
""".format(*params['operands'])

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    n = params['operands'][0]
    counter = 0
    while n > params['operands'][1]:
        if n > 0 and n % 2 == 0:
            n = n // 2
        else:
            n = n - params['operands'][2]
        counter = counter + 1

        if counter > 10000: # Just in case... although it should not happen.
            return -2

    if counter == int(answer):
        return 1
    else:
        return -1

#6.- especificar salida de un bucle for (dificultad baja).
def gcm_ex6_params():
    operands = list()
    operands.append(random.randint(-3, -1))
    operands.append(random.randint(-12, -10))
    operands.append(random.randint(-3, -2))

    params = dict()
    params['operands'] = operands
    
    return params

def gcm_ex6(solved):
    params = gcm_ex6_params()

    if solved:
        return -3

    msg = """Specify which value would be stored in the variable 'n' after the execution of the following program.
(Type "exit" (without quotes) to exit the program)

n = 1
for i in range({0}, {1}, {2}):
    n = n * i
""".format(*params['operands'])

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    n = 1
    for i in range(params['operands'][0], params['operands'][1], params['operands'][2]):
        n = n * i

    if n == int(answer):
        return 1
    else:
        return -1

#7.- especificar salida de un bucle for (dificultad más elevada).
def gcm_ex7_params():
    operands = list()
    operands.append(random.randint(1, 5))
    operands.append(operands[0] + random.randint(7, 11))

    params = dict()
    params['operands'] = operands

    return params

def gcm_ex7(solved):
    params = gcm_ex7_params()

    if solved:
        return -3

    msg = """Specify which value would be stored in the variable 'n' after the execution of the following program.
(Type "exit" (without quotes) to exit the program)

n = 0
g = 0
for i in range({0}, {1}, 1):
    if i % 3 == 0:
        g = g + 1
    else:
        n = n + g
""".format(*params['operands'])

    print(msg)
    answer = input("Answer: ")

    if answer == 'exit':
        return -2
    elif not isint(answer):
        return -1

    n = 0
    g = 0
    for i in range(params['operands'][0], params['operands'][1], 1):
        if i % 3 == 0:
            g = g + 1
        else:
            n = n + g

    if n == int(answer):
        return 1
    else:
        return -1

