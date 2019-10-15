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

    print('¿Cuál es el resultado de ejecutar la siguiente expresión?')
    print('Escribe la solución sin utilizar comillas')
    print('(Escribe "exit" (sin comillas) para salir del programa)')
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
    print(result)

    print('¿Cuál es el valor de la variable "resultado" (sin comillas) después de ejecutar el siguiente código para x = %d?' % param)
    print('Escribe la solución sin utilizar comillas')
    print('(Escribe "exit" (sin comillas) para salir del programa)')
    print('\t resultado=\'> \'')
    print('\t if x>7:')
    print('\t\t resultado = resultado + \'a \'')
    print('\t elif x//2==3:')
    print('\t\t resultado = resultado + \'b \'')
    print('\t if x+2>6:')
    print('\t\t resultado = resultado + \'c \'')

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

    print('¿Cuál es el valor de la variable "resultado" (sin comillas) después de ejecutar el siguiente código?')
    print('Escribe la solución sin utilizar comillas')
    print('(Escribe "exit" (sin comillas) para salir del programa)')
    print('\t resultado=\'> \'')
    print('\t for i in range(%d, %d ,%d):' % (param[0], param[1], param[2]))
    print('\t\t if i%2==0:')
    print('\t\t\t resultado = resultado + str(i) + \' \'')
    print('\t\t else:')
    print('\t\t\t resultado = resultado + str(i-1) + \' \'')

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

    print('¿Cuántas iteraciones hace el bucle interno del siguiente código?')
    print('(Escribe "exit" (sin comillas) para salir del programa)')
    print('\t for i in range(%d, %d ,%d):' % (param[0], param[1], param[2]))
    print('\t\t for i in range(%d, %d ,%d):' % (param[3], param[4], param[5]))
    print('\t\t\t print(i*j)')

    line = input()
    while not (is_int(line) or line == 'exit'):
        print('\nEscribe un número entero')
        print('¿Cuántas iteraciones hace el bucle interno del siguiente código?')
        print('(Escribe "exit" (sin comillas) para salir del programa)')
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

    print('Dado el número de teléfono \'' + telephone + '\', sustituye los puntos suspensivos en la siguiente línea de código')
    print('para tener el código del país en la variable "c" y el número en la variable "n" (sin comillas):')
    print('\t c, n = ...')
    print('(Escribe "exit" (sin comillas) para salir del programa)')

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

    print('Dada una lista con nombres de estudiantes almacenados en la variable "lista" (sin comillas), sustituye')
    print('los puntos suspensivos en la siguiente línea de código para imprimir el último nombre por orden alfabético:')
    print('\t print(...)')
    print('Denomina a la variable exactamente como "lista" (sin comillas)!')
    print('(Escribe "exit" (sin comillas) para salir del programa)')

    line = input()
    line = line.replace(" ", "")
    if (line.lower() == 'exit'):
        return -2
    elif (line == 'sorted(lista)[len(lista)-1]' or line == 'sorted(list)[-1]'):
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

    print('¿Qué devuelve la siguiente función si recibe la lista ' + str(param) + '?')
    print('\t def nueva_lista(lista):')
    print('\t\t for i in range(len(lista)):')
    print('\t\t\t lista[i] = lista[i] % 2 == 1')
    print('\t\t return lista')
    print('Usa el formato: [a, b, c, d, ...]')
    print('(Escribe "exit" (sin comillas) para salir del programa)')

    line = input()
    try:
        correct = type(eval(line)) is list
    except:
        correct = False

    while not (correct or line=='exit'):
        print('\nEscribe una lista con este formato: [a, b, c, d, ...]')
        print('¿Qué devuelve la siguiente función si recibe la lista ' + str(param) + '?')
        print('\t def int_lista(lista):')
        print('\t\t for i in range(len(lista)):')
        print('\t\t\t lista[i] = lista[i] % 2 == 1')
        print('\t\t return lista')
        print('(Escribe "exit" (sin comillas) para salir del programa)')
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
    names = ['olivia', 'marta', 'clara', 'sofia', 'isabel', 'juan', 'benjamin', 'martin', 'carlos', 'jorge']
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

    print('Dado el nombre \'' + param + '\', sustituye los puntos suspensivos en la próxima línea de código')
    print('para tener el nombre con la primera letra en mayúsculas (i.e. \'%s\')' % name_capital)
    print('en la variable "nombre" (sin comillas):')
    print('\t nombre = ...')
    print('Tienes que usar exactamente el nombre dado \'' + param + '\' y no una parte del mismo.')
    print('Usa len(\'' + param + '\') si necesitas el número de letras del nombre.')
    print('\ATENCIÓN!')
    print('En este ejercicio está prohibido usar los métodos upper() y lower().\n')
    print('(Escribe "exit" (sin comillas) para salir del programa)')

    line = input('name = ')
    line = line.replace(" ", "")
    if (line.lower() == 'exit'):
        return -2
    elif (line == result or line == result2):
        return 1
    else:
        return -1