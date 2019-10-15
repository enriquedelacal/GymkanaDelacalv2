"""
@author Noelia Rico noeliarico@uniovi.es
"""
import random

# Condicion que evalua a True para pares
def exN1(solved):
    
    if (solved):
        return -3
    
    print('''¿Cuál de las siguiente expresiones es evaluada a True cuando n es un número par enteros?''')
    print(' - a. n / 2 == 0')
    print(' - b. n % 2 == 1 ')
    print(' - c. n % 2 == 0')
    print(' - d. n / 2 == 1')
    print('(Escribe "exit" (sin comillas) para salir del programa)')
    identifier = input('>>> ')

    if (identifier=='exit'):
        return -2
    
    if (identifier not in ['a','b','c','d']):
        print('La opción que has introducido no es válida')
        return -1

    if identifier == 'c':
        return 1
    else:
        return -1

# Precedencia de los operadores logicos
def exN2(solved):
    
    if (solved):
        return -3
    
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)
    d = random.randint(0,10)
    cadena = '{} < {} and {} > {}'.format(a,b,c,d)
    real_value = a < b and c > d
    
    print('¿Cuál es el resultado al evaluar la siguiente expresión?:')
    print(cadena)
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    
    identifier = input('>>> ')
    
    if (identifier=='exit'):
        return -2
    
    if (real_value):
        if identifier in ['true', 'True']:
            return 1
        else :
            return -1
    else:
        if identifier in ['false', 'False']:
            return 1
        else:
            return -1
        
# Extraer elemento de una lista, muy facil
def exN3(solved):
    
    if (solved):
        return -3
    
    print('''Dada la siguiente lista:\n
                color_list = ["Red","Green","White" ,"Black"]\n
    Escribe en una línea el código necesario para obtener la palabra "White" de la lista sin modificarla.''')
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    identifier = input('>>> ')
    identifier = identifier.replace(" ", "")

    if (identifier=='exit'):
        return -2
    
    if (identifier=='color_list[2]'):
        return 1
    else:
        return -1

    
# Extraer mas de un elemento de una lista a la vez
def exN4(solved):
    
    if (solved):
        return -3
    
    print('''Dada la siguiente lista:\n
                color_list = ["Red","Green","White" ,"Black"]\n
    Escribe en una línea el código necesario para obtener ['Green', 'White', 'Black']''')
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    identifier = input('>>> ')
    identifier = identifier.replace(" ", "")

    if (identifier=='exit'):
        return -2
    
    if (identifier=='color_list[1:]' or identifier=='color_list[1:4]'):
        return 1
    else:
        return -1
    
# Utilizacion del operador + con strings
def exN5(solved):
    
    if (solved):
        return -3
    
    print("¿Cuál es el valor de n+n dada la variable n='3'?")
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    identifier = input('>>> ')
    possible_answers=["33", '"33"', "'33'"]
  
    if (identifier=='exit'):
        return -2
    
    if (identifier in possible_answers):
        return 1
    else:
        return -1

# extraccion de strings
def exN6(solved):
    
    if (solved):
        return -3
    
    print("Dada la variable my_text = 'Hello world!', escribe el código necesario para extraer 'lo w' del string")
    identifier = input('>>> ')
    identifier = identifier.replace(" ", "")
    
    sol = 'my_text[3:7]'

    if (identifier=='exit'):
        return -2
    
    if (identifier==sol):
        return 1
    else:
        return -1

# Multiplicacion y concatenacion de strings
def exN7(solved):
    
    if (solved):
        return -3
    
    print('''Dadas las variables a = '*' y b = 2. ¿Cuál es la salida de la siguiente expresión?:
                    a + a * b + a * b * b''')
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    identifier = input('>>> ')
    possible_answers=["*******", '"*******"', "'*******'"]
  
    if (identifier=='exit'):
        return -2
    
    if (identifier in possible_answers):
        return 1
    else:
        return -1

# Precedencia de los operadores logicos
def exN8(solved):
    
    if (solved):
        return -3
    
    a = random.randint(0,10)
    b = random.randint(0,10)
    # El valor va a depender siempre de lo que de > 
    cadena = '{} > {} and True or False and True'.format(a,b)
    real_value = a > b and True or False and True
    
    print('¿Cuál es la salida de la siguiente expresión?:\n')
    print(cadena)
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    
    identifier = input('>>> ')
    
    if (identifier=='exit'):
        return -2
    
    if (real_value):
        if identifier in ['true', 'True']:
            return 1
        else :
            return -1
    else:
        if identifier in ['false', 'False']:
            return 1
        else:
            return -1
        
# Precedencia de los operadores logicos
def exN9(solved):
    
    if (solved):
        return -3
    
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)
    cadena = '{0} == {1} or {0} < {2} and {2} > {1} '.format(a,b,c)
    real_value = a == b or a < c and c > b 
    
    print('¿Cuál es la salida de la siguiente expresión?:\n')
    print(cadena)
    print('Escribe "exit" (sin comillas) para salir del programa')
    
    identifier = input('>>> ')
    
    if (identifier=='exit'):
        return -2
    
    if (real_value):
        if identifier in ['true', 'True']:
            return 1
        else :
            return -1
    else:
        if identifier in ['false', 'False']:
            return 1
        else:
            return -1
