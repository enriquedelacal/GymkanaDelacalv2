# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:04:40 2018

@author: villa
"""
import re
import random

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
    

def jv_ex7(slvd):
	
    p = jv_ex7_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s([ ]+)in([ ]+)%s([ ]*)$"%(p[0], p[1]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = 34
    %s = %s

Write the line of code to test whether %s contains the value stored in %s.
>>>"""%(p[0],p[1],p[2],p[1],p[0]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1


#8.- comprobar si el valor contenido en una variable está en una lista 
def jv_ex8_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    s = "Artificial amateurs aren't at all amazing\n\tAnalytically, I assault, animate things"
    return [v, l, s]
    

def jv_ex8(slvd):
	
    p = jv_ex8_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s([ ]+)in([ ]+)%s([ ]*)$"%(p[0], p[1]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = 'Alphabet Aerobics'
    %s = "%s"

Write the line of code to test whether %s contains the value stored in %s.
>>>"""%(p[0],p[1],p[2],p[1],p[0]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1



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
    

def jv_ex6(slvd):
	
    p = jv_ex6_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s.extend[(]([ ]*)%s([ ]*)[)]([ ]*)$"%(p[1], p[0]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = %s
    %s = %s

Write the line of code to include the list %s at the end of %s without creating a new list, so the length of %s is incremented in the number of elements in %s.
>>>"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1], p[0]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1

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
    

def jv_ex9(slvd):
	
    p = jv_ex9_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s.append[(]([ ]*)%s([ ]*)[)]([ ]*)$"%(p[1], p[0]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = %s
    %s = %s

Write the line of code to include the list %s at the end of %s without creating a new list, so the length of %s is incremented in 1.
>>>"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1], p[1]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1





#5.- insertar un elemento en la lista a
def jv_ex5_params():
	v = chr(random.randint(ord('a'), ord('m')))
	l = chr(random.randint(ord('n'), ord('z')))
	mi = random.randint(-10, 10)
	ma = random.randint(mi + 3, mi + 10)
	s = random.random() * (ma - mi) + mi
	S = generateRandomFloatList(5, mi, ma)
	return [v, l, s, S]
    

def jv_ex5(slvd):
	
    p = jv_ex5_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s.append[(]([ ]*)%s([ ]*)[)]([ ]*)$"%(p[1], p[0]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = %s
    %s = %s

Write the line of code to introduce %s at the end of %s without creating a new list (+ operator is not valid, since it creates a new list).
>>>"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1



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
    

def jv_ex4(slvd):
	
    p = jv_ex4_params()
    
    if slvd:
        return -3
    
    ansRE =  re.compile("^%s([ ]+)in([ ]+)%s([ ]*)$"%(p[0], p[1]))
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = "%s"
    %s = %s

Write the line of code to test whether %s is included in %s or not.
>>>"""%(p[0], str(p[2]), p[1], str(p[3]), p[0], p[1]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE.match(answer):
        return 1
    else :
        return -1



#3.- dado una lista a, comprobar si el ultima posicion es de tipo entero
def jv_ex3_params():
	l = chr(random.randint(ord('n'), ord('z')))
	S = generateRandomFloatList(random.randint(4, 8), -10, 10)
	if random.random() <= 0.5:
		S[len(S) - 1] = random.randint(-10, 10)
	return [l, S]

def jv_ex3(slvd):
	
    p = jv_ex3_params()
	
    if slvd:
        return -3
	
    sols = ['type(' + p[0] + '[-1])isint']
    sols.append('type(' + p[0] + '[len(' + p[0] + ')-1])isint')
    sols.append('type(' + p[0] + '[-1])==int')
    sols.append('type(' + p[0] + '[len(' + p[0] + ')-1])==int')
    sols.append('isinstance(' + p[0] + '[-1],int)')
    sols.append('isinstance(' + p[0] + '[len(' + p[0] + ')-1],int)')
    solRE1 =  re.compile("^type\(%s\[-1\]\)==type\(int\(([-]?[0-9]+)?\)\)$"%(p[0]))
    solRE1bis =  re.compile("^type\(int\(([-]?[0-9]+)?\)\)==type\(%s\[-1\]\)$"%(p[0]))
    solRE2 =  re.compile("^type\(%s\[len\(%s\)-1\]\)==type\(int\(([-]?[0-9]+)?\)\)$"%(p[0],p[0]))
    solRE2bis =  re.compile("^type\(int\(([-]?[0-9]+)?\)\)==type\(%s\[len\(%s\)-1\]\)$"%(p[0],p[0]))
    solRE3 =  re.compile("^type\(%s\[len\(%s\)-1\]\)==type\(int\(%s\[len\(%s\)-1\]\)\)$"%(p[0],p[0],p[0],p[0]))
    solRE4 =  re.compile("^type\(int\(%s\[len\(%s\)-1\]\)\)==type\(%s\[len\(%s\)-1\]\)$"%(p[0],p[0],p[0],p[0]))
    solRE5 =  re.compile("^type\(%s\[-1\]\)==type\(int\(%s\[-1\]\)\)$"%(p[0],p[0]))
    solRE6 =  re.compile("^type\(int\(%s\[-1\]\)\)==type\(%s\[-1\]\)$"%(p[0],p[0]))
    solRE7 =  re.compile("^type\(%s\[len\(%s\)-1\]\)==type\(int\(%s\[-1\]\)\)$"%(p[0],p[0],p[0]))
    solRE8 =  re.compile("^type\(int\(%s\[-1\]\)\)==type\(%s\[len\(%s\)-1\]\)$"%(p[0],p[0],p[0]))
    solRE9 =  re.compile("^type\(%s\[-1\]\)==type\(int\(%s\[len\(%s\)-1\]\)\)$"%(p[0],p[0],p[0]))
    solRE10 =  re.compile("^type\(int\(%s\[len\(%s\)-1\]\)\)==type\(%s\[-1\]\)$"%(p[0],p[0],p[0]))
	
	
##    ansRE1 =  re.compile("^type([ ]*)\(([ ]*)%s([ ]*)\[([ ]*)len\(([ ]*)%s([ ]*)\)([ ]*)-([ ]*)1([ ]*)\]([ ]*)\)([ ]*)==([ ]*)type([ ]*)\(([ ]*)int([ ]*)\(([ ]*)([0-9]+([ ]*))?\)([ ]*)\)([ ]*)$"%(p[0], p[0]))
##    ansRE2 =  re.compile("^type([ ]*)\(([ ]*)%s([ ]*)\[([ ]*)[-]([ ]*)1([ ]*)\]([ ]*)\)([ ]*)==([ ]*)type([ ]*)\(([ ]*)int([ ]*)\(([ ]*)([0-9]+([ ]*))?\)([ ]*)\)([ ]*)$"%(p[0]))
#    ansRE1 =  re.compile("^type\(([ ]*)%s\[([ ]*)len\(([ ]*)%s([ ]*)\)([ ]*)-([ ]*)1([ ]*)\]([ ]*)\)([ ]*)==([ ]*)type\(([ ]*)int\(([ ]*)([0-9]+([ ]*))?\)([ ]*)\)([ ]*)$"%(p[0], p[0]))
#    ansRE2 =  re.compile("^type\(([ ]*)%s\[([ ]*)[-]([ ]*)1([ ]*)\]([ ]*)\)([ ]*)==([ ]*)type\(([ ]*)int\(([ ]*)([0-9]+([ ]*))?\)([ ]*)\)([ ]*)$"%(p[0]))
	
    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = %s

Write the line of code to test if the last element in %s is an integer.
You must use either len to obtain the position of the last element or negative indexes.
Use type(int(1)) to obtain the type of an integer.
>>>"""%(p[0], str(p[1]), p[0]) 
    
    #print(msg)
    
    answer = input(msg)
    answer = answer.replace(" ", "")
    
    if answer == 'exit':
        return -2
    elif solRE1.match(answer) or solRE2.match(answer):
        return 1
    elif solRE3.match(answer) or solRE4.match(answer):
        return 1
    elif solRE5.match(answer) or solRE6.match(answer):
        return 1
    elif solRE7.match(answer) or solRE8.match(answer):
        return 1
    elif solRE9.match(answer) or solRE10.match(answer):
        return 1
    elif solRE1bis.match(answer) or solRE2bis.match(answer):
        return 1
    elif answer in sols:
        return 1
    else :
        return -1
    
#    if answer == 'exit':
#        return -2
#    elif ansRE1.match(answer):
#        return 1
#    elif ansRE2.match(answer):
#        return 1
#    else :
#        return -1


#2.- dada una cadena s, comprobar si la primera letra es minúscula usando lower
def jv_ex2_params():
	l = chr(random.randint(ord('n'), ord('z')))
	S = generateRandomStr(8)
	return [l, S]

def jv_ex2(slvd):
	
    p = jv_ex2_params()
	
    if slvd:
        return -3
	
    ansRE1 =  re.compile("^%s\[([ ]*)0([ ]*)\].lower\(([ ]*)\)([ ]*)==([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))
    ansRE2 =  re.compile("^([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)==([ ]*)%s\[([ ]*)0([ ]*)\].lower\(([ ]*)\)([ ]*)$"%(p[0], p[0]))
	
    ansRE3 =  re.compile("^%s.lower\(([ ]*)\)\[([ ]*)0([ ]*)\]([ ]*)==([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))
    ansRE4 =  re.compile("^([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)==([ ]*)%s.lower\(([ ]*)\)\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))
    

    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = "%s"

Write the line of code to test if the first element in %s is in lowercase.
You MUST use the method lower() to obtain the str in lowercase.
>>>"""%(p[0], str(p[1]), p[0]) 
    
    #print(msg)
    
    answer = input(msg)
    
    if answer == 'exit':
        return -2
    elif ansRE1.match(answer):
        return 1
    elif ansRE2.match(answer):
        return 1
    elif ansRE3.match(answer):
        return 1
    elif ansRE4.match(answer):
        return 1
    else :
        return -1

#2.- dada una cadena s, comprobar si la primera letra es minúscula usando lower
def jv_ex10_params():
	l = chr(random.randint(ord('n'), ord('z')))
	S = generateRandomStr(8)
	return [l, S]

def jv_ex10(slvd):
	
    p = jv_ex10_params()
	
    if slvd:
        return -3
	
    ansRE1 =  re.compile("^%s\[([ ]*)0([ ]*)\]([ ]*)>=([ ]*)'a'([ ]+)and([ ]+)%s(\[([ ]*)0([ ]*)\][ ]*)<=([ ]*)'z'([ ]*)$"%(p[0], p[0]))
    ansRE2 =  re.compile("^'a'([ ]*)<=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]+)and([ ]+)'z'([ ]*)>=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))
    ansRE3 =  re.compile("^%s\[([ ]*)0([ ]*)\]([ ]*)<=([ ]*)'z'([ ]+)and([ ]+)%s\[([ ]*)0([ ]*)\]([ ]*)>=([ ]*)'a'([ ]*)$"%(p[0], p[0]))
    ansRE4 =  re.compile("^'z'([ ]*)>=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]+)and([ ]+)'a'([ ]*)<=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))
	
    ansRE5 =  re.compile("^'a'([ ]*)<=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]+)and([ ]+)%s\[([ ]*)0([ ]*)\]([ ]*)<=([ ]*)'z'([ ]*)$"%(p[0], p[0]))
    ansRE6 =  re.compile("^%s\[([ ]*)0([ ]*)\]([ ]*)>=([ ]*)'a'([ ]+)and([ ]+)'z'([ ]*)>=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))

    ansRE7 =  re.compile("^'z'([ ]*)>=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]+)and([ ]+)%s\[([ ]*)0([ ]*)\]([ ]*)>=([ ]*)'a'([ ]*)$"%(p[0], p[0]))
    ansRE8 =  re.compile("^%s\[([ ]*)0([ ]*)\]([ ]*)<=([ ]*)'z'([ ]+)and([ ]+)'a'([ ]*)<=([ ]*)%s\[([ ]*)0([ ]*)\]([ ]*)$"%(p[0], p[0]))


    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = "%s"

Write the line of code to test if the first element in %s is in lowercase.
You MUST ONLY use comparison operators (the use of ord() and chr() is forbidden).
>>>"""%(p[0], str(p[1]), p[0]) 
    
    #print(msg)
    
    answer = input(msg).replace('"',"'")
    
    if answer == 'exit':
        return -2
    elif ansRE1.match(answer):
        return 1
    elif ansRE2.match(answer):
        return 1
    elif ansRE3.match(answer):
        return 1
    elif ansRE4.match(answer):
        return 1
    elif ansRE5.match(answer):
        return 1
    elif ansRE6.match(answer):
        return 1
    elif ansRE7.match(answer):
        return 1
    elif ansRE8.match(answer):
        return 1
    else :
        return -1


#1.- dentro de un intervalo genérico para cualquier lenguaje de programacion
def jv_ex1_params():
    v = chr(random.randint(ord('a'), ord('m')))
    l = chr(random.randint(ord('n'), ord('z')))
    while l == v:
        l = chr(random.randint(ord('n'), ord('z')))
    m = chr(random.randint(ord('a'), ord('z')))
    while m == v or m == l:
        m = chr(random.randint(ord('a'), ord('z')))
    s = random.randint(-10, 10)
    S = random.randint(s+1, s+10)
    M = random.randint(-10, 10)

    return [v, l, m, s, S, M]

def jv_ex1(slvd):
	
    p = jv_ex1_params()
	
    if slvd:
        return -3
	
    ansRE1 =  re.compile("^%s([ ]*)>=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)<=([ ]*)%s([ ]*)$"%(p[2], p[0], p[2], p[1])) #m>=v and m<=l
    ansRE2 =  re.compile("^%s([ ]*)<=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)>=([ ]*)%s([ ]*)$"%(p[2], p[1], p[2], p[0])) #m<=l and m>=v
    ansRE3 =  re.compile("^%s([ ]*)>=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)<=([ ]*)%s([ ]*)$"%(p[1], p[2], p[0], p[2])) #l>=m and v<=m
    ansRE4 =  re.compile("^%s([ ]*)<=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)>=([ ]*)%s([ ]*)$"%(p[0], p[2], p[2], p[0])) #v<=m and l>=m

    ansRE5 =  re.compile("^%s([ ]*)<=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)<=([ ]*)%s([ ]*)$"%(p[0], p[2], p[2], p[1])) #v<=m and m<=l
    ansRE6 =  re.compile("^%s([ ]*)>=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)>=([ ]*)%s([ ]*)$"%(p[2], p[0], p[1], p[2])) #m>=v and l>=m

    ansRE7 =  re.compile("^%s([ ]*)>=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)>=([ ]*)%s([ ]*)$"%(p[1], p[2], p[2], p[0])) #l>=m and m>=v
    ansRE8 =  re.compile("^%s([ ]*)<=([ ]*)%s([ ]+)and([ ]+)%s([ ]*)<=([ ]*)%s([ ]*)$"%(p[2], p[1], p[0], p[2])) #m<=l and v<=m

    
    msg = """======================================
TYPE -->exit<-- to EXIT the progam.

You have the following code:
    %s = %d
    %s = %d
    %s = %d

Write the line of code to test if %s belongs to [%s, %s].
You MUST ONLY use comparison operators.
Do not use nested comparisons (e.g., a<b<c<d).
>>>"""%(p[0], p[3], p[1], p[4], p[2], p[5], p[2], p[0], p[1]) 
    
    #print(msg)
    
    answer = input(msg).replace('"',"'")
    
    if answer == 'exit':
        return -2
    elif ansRE1.match(answer):
        return 1
    elif ansRE2.match(answer):
        return 1
    elif ansRE3.match(answer):
        return 1
    elif ansRE4.match(answer):
        return 1
    elif ansRE5.match(answer):
        return 1
    elif ansRE6.match(answer):
        return 1
    elif ansRE7.match(answer):
        return 1
    elif ansRE8.match(answer):
        return 1
    else :
        return -1



