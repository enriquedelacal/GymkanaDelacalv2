# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:04:40 2018

@author: villa
"""
import common
import re
import random

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


#def raw_input(msg):
#    return input(msg)


def generateRandomStr(lon):
    s = ''
    while len(s) < lon:
        s = s + chr(random.randint(ord('a'), ord('z')))
    return s


def generateRandomStrList(lon, includeStr = ''):
    incluida = False
    incluir = (len(includeStr) != 0)
    l = [''] * lon
    for i in range(lon):
        if incluir and not incluida and random.random() <= (1.0 / lon):
            l[i] = includeStr
            incluida= True
        else:
            l[i] = generateRandomStr(random.randint(4, 8))
    if incluir and not incluida:
        l[random.randint(0, len(l) - 1)] = includeStr
    return l


def generateRandomIntegerList(lon, mi=-10, ma=10):
    l = [0] * lon
    for i in range(lon):
        l[i] = random.randint(mi, ma)
    return l


def generateRandomFloatList(lon, mi=-10, ma=10):
    l = [0] * lon
    for i in range(lon):
        l[i] = random.random() * (ma - mi) + mi
    return l


###############################################################################
###############################################################################
#7.- comprobar si el valor contenido en una variable está en una lista 
def jv_ex7_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    mi = random.randint(1, 10)
    ma = mi + 4
    s = str(list(range(mi, ma)))
    return [v, l, s]
    

def jv_ex7():
    p = jv_ex7_params()
    
    ansRE =  re.compile("^%s([ ]+)in([ ]+)%s([ ]*)$"%(p[0], p[1]))
    
    msg = {'EN_US':"""You have the following code:
    %s = 34
    %s = %s

Write the line of code to test whether %s contains the value stored in %s.
"""%(p[0],p[1],p[2],p[1],p[0]),
           'ES_ES':"""You have the following code:
    %s = 34
    %s = %s

Write the line of code to test whether %s contains the value stored in %s.
"""%(p[0],p[1],p[2],p[1],p[0])}[common.LANG]

    print(msg)
    answer = input('>>> ')
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1


###############################################################################
###############################################################################
#8.- comprobar si el valor contenido en una variable está en una cadena 
def jv_ex8_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    s = "Artificial amateurs aren't at all amazing\n\tAnalytically, I assault, animate things"
    return [v, l, s]
    

def jv_ex8():
    p = jv_ex8_params()
    
    ansRE =  re.compile("^%s([ ]+)in([ ]+)%s([ ]*)$"%(p[0], p[1]))
    
    msg = {'EN_US':"""You have the following code:
    %s = 'Alphabet Aerobics'
    %s = "%s"

Write the line of code to test whether %s contains the value stored in %s.
"""%(p[0],p[1],p[2],p[1],p[0]),
           'ES_ES':"""You have the following code:
    %s = 'Alphabet Aerobics'
    %s = "%s"

Write the line of code to test whether %s contains the value stored in %s.
"""%(p[0],p[1],p[2],p[1],p[0])}[common.LANG]
    
    print(msg)
    answer = input('>>> ')
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1


###############################################################################
###############################################################################
#6.- insertar la lista [1,2,3] en la lista a como elementos individuales
def jv_ex6_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    mi = random.randint(1, 10)
    ma = random.randint(mi+2, mi + 4)
    s = list(range(mi, ma))
    mi = random.randint(-10, 10)
    ma = random.randint(mi+2, mi + 7)
    S = list(range(mi, ma))
    return [v, l, s, S]


def jv_ex6():
    repite = True
    while repite:
        p = jv_ex6_params()
        
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = %s
%s = %s"""%(p[0], str(p[2]), p[1], str(p[3]))
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            repite = False
            #print(loc)
            solucion = list(p[3])
            solucion.extend(p[2])
        except SyntaxError as e:
            repite = True
            print(e)

    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion
    msg = {'EN_US':"""You have the following code:
    %s = %s
    %s = %s

Write the line of code to include the list %s at the end of %s without creating a new list, so the length of %s is incremented in the number of elements in %s.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1], p[0]),
           'ES_ES':"""Dado el siguiente codigo:
    %s = %s
    %s = %s

Escribe la expresión para incluir la lista %s al final de %s sin crear una nueva lista, de forma que la longitud de %s se incremente en el número de elementos de %s.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1], p[0])}[common.LANG]

    print(msg)
    answer = input('>>> ')
    #print(answer)
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        #evitemos que el usuario haga trampas: por ejemplo, crear la lista con los valores directamente
        if "[" in answer or "]" in answer:
            print("Sorry, but you do not need the brackets ([ o ]) to solve this problem.")
            print("Better to try again.")
            return -1

        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            if p[1] in loc:
                if loc[p[1]] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable que no es 
                   #igual a nuestra solucion, luego hay errores.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#9.- insertar la lista [1,2,3] en la lista a como un único elemento
def jv_ex9_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    mi = random.randint(1, 10)
    ma = random.randint(mi+2, mi + 4)
    s = list(range(mi, ma))
    mi = random.randint(-10, 10)
    ma = random.randint(mi+2, mi + 7)
    S = list(range(mi, ma))
    return [v, l, s, S]


def jv_ex9():
    repite = True
    while repite:
        p = jv_ex9_params()
        
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = %s
%s = %s"""%(p[0], str(p[2]), p[1], str(p[3]))
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = list(p[3])
            solucion.append(p[2])
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)

    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion
    msg = {'EN_US':"""You have the following code:
    %s = %s
    %s = %s

Write the line of code to include the list %s at the end of %s without creating a new list, so the length of %s is incremented in 1.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1]),
           'ES_ES':"""Dado el siguiente código:
    %s = %s
    %s = %s

Escribe la expresión para incluir la lista %s al final de %s sin crear una nueva lista, de manera que la longitud de %s se incremente en 1.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1])}[common.LANG]

    print(msg)
    answer = input('>>> ')

    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        #evitemos que el usuario haga trampas: por ejemplo, crear la lista con los valores directamente
        if "[" in answer or "]" in answer:
            print("Sorry, but you do not need the brackets ([ o ]) to solve this problem.")
            print("Better to try again.")
            return -1
        
        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            if p[1] in loc:
                if loc[p[1]] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable que no es 
                   #igual a nuestra solucion, luego hay errores.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#5.- insertar un elemento en la lista a
def jv_ex5_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    mi = random.randint(-10, 10)
    ma = random.randint(mi + 3, mi + 10)
    s = random.random() * (ma - mi) + mi
    S = generateRandomFloatList(5, mi, ma)
    return [v, l, s, S]
    

def jv_ex5():
    repite = True
    while repite:
        p = jv_ex5_params()
        
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = %s
%s = %s"""%(p[0], str(p[2]), p[1], str(p[3]))
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = list(p[3])
            solucion.append(p[2])
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)

    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion
    msg = {'EN_US':"""You have the following code:
    %s = %s
    %s = %s

Write the line of code to introduce %s at the end of %s without creating a new list (+ operator is not valid, since it creates a new list).
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1]),
           'ES_ES':"""Dado el siguiente código:
    %s = %s
    %s = %s

Escribe la expresión que introduce %s al final de %s sin crear una nueva lista (el operador + no es válido, ya que crea una nueva lista).
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1])}[common.LANG]
    
    print(msg)
    answer = input('>>> ')
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        #evitemos que el usuario haga trampas: por ejemplo, crear la lista con los valores directamente
        if "[" in answer or "]" in answer:
            print("Sorry, but you do not need the brackets ([ o ]) to solve this problem.")
            print("Better to try again.")
            return -1

        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            if p[1] in loc:
                if loc[p[1]] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable que no es 
                   #igual a nuestra solucion, luego hay errores.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#4.- dada una lista a, evaluar si contien la str "amigo"
def jv_ex4_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    s = generateRandomStr(5)
    if random.random() <= 0.5:
        S = generateRandomStrList( random.randint(4, 6), s)
    else:
        S = generateRandomStrList( random.randint(4, 6))
    return [v, l, s, S]


def jv_ex4():
    repite = True
    while repite:
        p = jv_ex4_params()
        
        #print(p)
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = '%s'
%s = %s"""%(p[0], str(p[2]), p[1], str(p[3]))
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = p[2] in p[3]
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)
            
    
    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion    
    output_variable_name = "outcome"
    ansRE =  re.compile("^%s([ ]*)=([ ]*)%s([ ]+)in([ ]+)%s([ ]*)$"%(output_variable_name,p[0], p[1]))
    
    msg = {'EN_US':"""You have the following code:
    %s = "%s"
    %s = %s

Write the line of code to test whether %s is included in %s or not, storing the result in a variable called %s.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], output_variable_name),
           'ES_ES':"""Dado el siguiente código:
    %s = "%s"
    %s = %s

Escribe la expresión que determine si %s esta incluida en $s o no. Almacena el resultado en una variable denominada %s.
"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], output_variable_name)}[common.LANG]

    print(msg)
    answer = input('>>> ')
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
         #evitemos que el usuario haga trampas: por ejemplo, asignar True or False directamente!
        if "True" in answer or "False" in answer:
            print("Sorry, but you do not need a boolean constant to solve this problem.")
            print("Better to try again.")
            return -1
        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            #print(f'output {output_variable_name},\n loc {loc}\n' + 10*'=' + '\n' )
            if output_variable_name in loc:
                #print(f'ansRE.match == {ansRE.match(answer)}')
                if loc[output_variable_name] == solucion and ansRE.match(answer):
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable  con el nombre 
                   #deseado pero con un valor diferente a nuestra solucion o 
                   #bien es un codigo diferente.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#3.- dado una lista a, comprobar si el ultima posicion es de tipo entero
#    debe usarse el operador is o la función isinstance.
def jv_ex3_params():
    l = chr(random.randint(ord('n'), ord('z')))
    S = generateRandomFloatList(random.randint(4, 8), -10, 10)
    if random.random() <= 0.5:
        S[len(S) - 1] = random.randint(-10, 10)
    return [l, S]


def jv_ex3():
    p = jv_ex3_params()

    sols = '(type\(' + p[0] +               '\[-1\]\)isint)|'
    sols = sols + '(^type\(' + p[0] +       '\[-1\]\)==int$)|'
    sols = sols + '(^isinstance\(' + p[0] + '\[-1\],int\)$)|'
    sols = sols + '(^type\(' + p[0] +       '\[len\(' + p[0] + '\)-1\]\)isint$)|'
    sols = sols + '(^type\(' + p[0] +       '\[len\(' + p[0] + '\)-1\]\)==int$)|'
    sols = sols + '(^isinstance\(' + p[0] + '\[len\(' + p[0] + '\)-1\],int\)$)'
    ansRE =  re.compile(sols)
    
    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion    
    msg = {'EN_US':"""You have the following code:
    %s = %s

Write the expression to test if the last element in %s is an integer. 
You must use either len to obtain the position of the last element or negative indexes.
You should use either:
*    the operator is together with the function type, or 
*    the operator == with the function type, or
*    the function isinstance.
Maybe you might want to look for help on these topics.

"""%(p[0], str(p[1]), p[0]),
           'ES_ES':"""Dado el siguiente código:
    %s = %s

Escribe la expresión para evaluar si el último elemento en %s es un entero.
Puede usar bien len para obtener la posición del último elemento o bien índices negativos.
Además, debes usar una de las siguientes opciones:
*    el operador is conjuntamente con la función type, o
*    el operador == con la función type, o
*    la función isinstance.
Quizás debería buscar ayuda sobre estas funciones (help).

"""%(p[0], str(p[1]), p[0])}[common.LANG]

    print(msg)
    answer = input('>>> ')
    ansSinSpaces = answer.replace(" ", "")
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        try:
            if ansRE.match(ansSinSpaces):
                return 1
            else :
                return -1
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#2.- dada una cadena s, comprobar si la primera letra es minúscula usando lower
def jv_ex2_params():
    l = chr(random.randint(ord('n'), ord('z')))
    S = generateRandomStr(8)
    return [l, S]


def jv_ex2():
    repite = True
    while repite:
        p = jv_ex2_params()
        
        #print(p)
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s =  '%s'"""%(p[0], str(p[1]))
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        loc = add_getitem_str_to_local_dictionary(loc)
        
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = p[1].lower()[0] == p[1][0]
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)
            
    
    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion    
    output_variable_name = "outcome"
    msg = {'EN_US':"""You have the following code:
    %s = "%s"

Write the line of code to test if the first element in %s is in lowercase.
Store the result in a variable called %s.
You can use the method you want to solve this, but keeping it simple.
"""%(p[0], str(p[1]), p[0], output_variable_name),
           'ES_ES':"""Dado el siguiente código:
    %s = "%s"

Escribe la expresión que evalúa si el primer elemento en %s está en minúsculas.
Almacena el resultado en una variable denominada %s.
Puedes utilizar cualquier método para solucionar el problema, pero que sea simple.

"""%(p[0], str(p[1]), p[0], output_variable_name)}[common.LANG]

    print(msg)
    answer = input('>>> ')
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        #evitemos que el usuario haga trampas: por ejemplo, asignar True or False directamente!
        if "True" in answer or "False" in answer:
            print("Sorry, but you do not need a boolean constant to solve this problem.")
            print("Better to try again.")
            return -1
        
        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            #print(f'output {output_variable_name},\n loc {loc}\n' + 10*'=' + '\n' )
            if output_variable_name in loc:
                #print(f'ansRE.match == {ansRE.match(answer)}')
                if loc[output_variable_name] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable  con el nombre 
                   #deseado pero con un valor diferente a nuestra solucion o 
                   #bien es un codigo diferente.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#2.- dada tres cadenas, substituir en la primera de ellas las ocurrencias de 
#la segunda por la tercera
def jv_ex10_params():
    l = chr(random.randint(ord('n'), ord('z')))
    S = generateRandomStr(8)
    l2 = chr(random.randint(ord('n'), ord('z')))
    S2 = generateRandomStr(8)
    l3 = chr(random.randint(ord('n'), ord('z')))
    S3 = generateRandomStr(8)
    return [l, S, l2, S2, l3, S3]


def jv_ex10():
    repite = True
    while repite:
        p = jv_ex10_params()
        
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = '%s'
%s = '%s'
%s = '%s'"""%(p[0], p[1], p[2], p[3], p[4], p[5])
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        loc = add_getitem_str_to_local_dictionary(loc)
        
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = p[1].replace(p[3], p[5])
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)
    
    
    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion    
    output_variable_name = 'outcome'
    msg = {'EN_US':"""You have the following code:
    %s = '%s'
    %s = '%s'
    %s = '%s'

Write the line of code so all the occurrences of %s in %s are substituted by %s.
Store the produced str in a variable called %s
"""%(p[0], p[1], p[2], p[3], p[4], p[5], p[2], p[0], p[4], output_variable_name),
           'ES_ES':"""Dado el siguiente código:
    %s = '%s'
    %s = '%s'
    %s = '%s'

Escribe la línea de código de manera que todas las ocurrencias de %s en %s se sustituyan por %s.
Almacena la str resultado en una variable denominada %s.
"""%(p[0], p[1], p[2], p[3], p[4], p[5], p[2], p[0], p[4], output_variable_name)}[common.LANG]
    
    print(msg)
    answer = input('>>> ')
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        
        #evitemos que el usuario haga trampas: por ejemplo, asignar la cadena resultado directamente!
        if solucion in answer :
            print("Sorry, you don't need to type {solucion} in the code: that is the expected value to obtain!")
            print("Better to try again.")
            return -1
        
        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            #print(f'output {output_variable_name},\n loc {loc}\n' + 10*'=' + '\n' )
            if output_variable_name in loc:
                #print(f'ansRE.match == {ansRE.match(answer)}')
                if loc[output_variable_name] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable  con el nombre 
                   #deseado pero con un valor diferente a nuestra solucion o 
                   #bien es un codigo diferente.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


###############################################################################
###############################################################################
#1.- dentro de un intervalo genérico para cualquier lenguaje de programacion
def jv_ex1_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    m = chr(random.randint(ord('a'), ord('z')))
    while m == v or m == l:
        m = chr(random.randint(ord('a'), ord('z')))
    minV = -20
    maxV = 50
    shift = 10
    lowerBound = random.randint(minV, maxV)
    upperBound = random.randint(lowerBound + 1, max(lowerBound + shift, maxV))
    thirdValue = random.randint(minV, maxV)
    return [v, l, m, lowerBound, upperBound, thirdValue]


def jv_ex1():
    repite = True
    while repite:
        p = jv_ex1_params()
        
        #Esta es el codigo que muetro en el mensaje de mas abajo describiendo el
        #ejercicio al estudiante. Ejecutare ese codigo para crear las variables
        #de contexto para el ejercicio.
        myCode = """
%s = '%s'
%s = '%s'
%s = '%s'"""%(p[0], p[3], p[1], p[4], p[2], p[5])
    
        total = create_secure_dict()
        
        loc = initialize_local_dict()
        loc = add_getitem_str_to_local_dictionary(loc)
        
        try:
            byte_code = compile_restricted(
                myCode,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #En este momento, loc es un diccionario con dos listas
            #print(loc)

            #se obtiene la solucion
            solucion = p[5] >= p[3] and p[5] <= p[4]
            
            #y si todo va bien, no se repite
            repite = False

        except SyntaxError as e:
            repite = True
            print(e)

    #Ahora muestro el ejercicio al estudiante y pido su codigo solucion    
    output_variable_name = 'outcome'
    msg = {'EN_US':"""You have the following code:
    %s = %d
    %s = %d
    %s = %d

Write the line of code to test if %s belongs to [%s, %s].
You MUST ONLY use comparison operators.
Store the result of the comparison in a variable called %s.
Do not use nested comparisons (e.g., a<b<c<d).
"""%(p[0], p[3], p[1], p[4], p[2], p[5], p[2], p[0], p[1], output_variable_name),
           'ES_ES':"""Dado el siguiente código:
    %s = %d
    %s = %d
    %s = %d

Escribe la línea de código para evaluar si %s pertenece al intervalo [%s, %s].
Solo se pueden utilizar operadores de comparación.
ALmacena el resultado de la comparación en una variable denominada %s.
No anides comparaciones (e.g., a<b<c<d).
"""%(p[0], p[3], p[1], p[4], p[2], p[5], p[2], p[0], p[1], output_variable_name)}[common.LANG]

    print(msg)
    answer = input('>>> ')
    
    #Ahora toca comprobar que ocurre con la respuesta del estudiante:    
    if answer == 'exit':
        return -2
    else:
        #evitemos que el usuario haga trampas: por ejemplo, asignar True or False directamente!
        if "True" in answer or "False" in answer:
            print("Sorry, but you do not need a boolean constant to solve this problem.")
            print("Better to try again.")
            return -1
        if 'and' not in answer and 'or' not in answer:
            print("I am afraid you have not used logical operators.")
            print("Better to try again.")
            return -1
        try:
            byte_code = compile_restricted(
                answer,
                filename='<inline code>',
                mode='exec'
            )
            exec(byte_code, {'__builtins__': total}, loc)
            #print(loc)
            #print(f'output {output_variable_name},\n loc {loc}\n' + 10*'=' + '\n' )
            if output_variable_name in loc:
                #print(f'ansRE.match == {ansRE.match(answer)}')
                if loc[output_variable_name] == solucion:
                   #En este caso, el codigo es correcto y la variable obtenida
                   #es igual a nuestra solucion
                   return 1
                else :
                   #pEn este caso, el codigo genera una variable  con el nombre 
                   #deseado pero con un valor diferente a nuestra solucion o 
                   #bien es un codigo diferente.
                   return -1
            else:
                #En este caso, el codigo introducido no ha generado la variable
                #que hemos pedido crear o modificar
                return -1
        except SyntaxError as e:
            #en este caso existe un error sintactico
            #Por si las moscas, se muestra por pantalla.
            print("Error in source_code: ", e)
            print("This error forces to stop playing, I'm afraid")
            print("Try again; if it happens again then send a message to your teacher.")
            return -2
        except:
            #En este caso, se han usado palabras reservadas catalogadas como no
            #seguras. Se muestra el mensaje de no usar print, acceso a archivos...
            print("This error in the source code is not secure!")
            print("Do not use print, nor file access or the os package!")
            return -1


if __name__=='__main__':
    print(jv_ex6())
