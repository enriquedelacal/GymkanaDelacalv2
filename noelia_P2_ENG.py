"""
@author Noelia Rico noeliarico@uniovi.es
"""
import random

# Condicion que evalua a True para pares
def exN1(solved):
    
    if (solved):
        return -3
    
    print('''Which of the following conditions will be evaluated as True for integer even numbers?''')
    print(' - a. n / 2 == 0')
    print(' - b. n % 2 == 1 ')
    print(' - c. n % 2 == 0')
    print(' - d. n / 2 == 1')
    print('(Type "exit" (without quotes) to exit the program)')
    identifier = raw_input('>>> ')

    if (identifier=='exit'):
        return -2
    
    if (identifier not in ['a','b','c','d']):
        print('Invalid option!')
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
    
    print('What is the output of the following expression?:')
    print(cadena)
    print('(Type "exit" (without quotes) to exit the program)')
    
    
    identifier = raw_input('>>> ')
    
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
    
    print('''Given the following list:\n
                color_list = ["Red","Green","White" ,"Black"]\n
    Write the code that would be necessary to get the word "White" from the list without modifying the it.''')
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
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
    
    print('''Given the following list:\n
                color_list = ["Red","Green","White" ,"Black"]\n
    Write one line of code to get the output ['Green', 'White', 'Black']''')
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
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
    
    print("What's the value of n+n if we have the variable n='3'")
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
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
    
    print("Given the variable my_text = 'Hello world!' write the code necessary to extract 'lo w' from the string")
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
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
    
    print('''Given the variables a = '*' and b = 2. What is the output of the following expresion?:
                    a + a * b + a * b * b''')
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
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
    
    print('What is the output of the following expression?:\n')
    print(cadena)
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
    
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
    
    print('What is the output of the following expression?:')
    print(cadena)
    print('(Type "exit" (without quotes) to exit the program)')
    
    identifier = raw_input('>>> ')
    
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
