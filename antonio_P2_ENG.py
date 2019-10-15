

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Antonio
#
# Created:     30/05/2018
# Copyright:   (c) Antonio 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import time
import re


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def ex1_ant_params():
    actualParam = [random.choice([-1,1])]
    actualParam += [random.choice([2,3,4])]
    actualParam += [random.choice([2,3])]
    actualParam += [5-actualParam[2]]
    return actualParam


# Return:  
#     -3: Already solved
#     -2: Exit
#     -1: Incorrect sol.
#      1: Correct sol.
def ex1_ant(resuelto):
    actualParam = ex1_ant_params()
    if (resuelto):
        return -3

    sign = ''
    if (actualParam[0]==-1):
        sign = '-'

    resul = actualParam[0]*(actualParam[1]**actualParam[2]**actualParam[3])
    print'What gets printed after executing the following piece of code?'
    print '(Type "exit" (without quotes) to exit the program)'
    print '>>> ' + sign + str(actualParam[1]) + '**' + str(actualParam[2]) + '**' + str(actualParam[3])
    line = raw_input()
    while not (check_int(line) or line=='exit'):
        print '\nYou must type a positive integer'
        print 'What gets printed after executing the following piece of code?'
        print '(Type "exit" (without quotes) to exit the program)'
        print '>>> ' + sign + str(actualParam[1]) + '**' + str(actualParam[2]) + '**' + str(actualParam[3])
        line = raw_input()

    if (line.lower()=='exit'):
        return -2

    line = int(line)

    if (line==resul):
        return 1
    else:
        return -1


def ex2_ant_params():
    param = [random.randint(1,9)]
    param += [random.randint(4,12)]
    param += [random.choice([-1,1,2])]
    return param

def ex2_ant(resuelto):
    param = ex2_ant_params()
    if (resuelto):
        return -3

    print 'What is the result of executing the following sentence?'
    print 'Use this format: [a, b, c, d, ...]'
    print '(Type "exit" (without quotes) to exit the program)'
    print '>>> range(' + str(param[0]) + ', ' + str(param[1]) + ', ' + str(param[2]) + ')'
    resul = list(range(param[0], param[1], param[2]))
    line = raw_input()
    try:
        correct = type(eval(line)) is list
    except:
        correct = False
    while not (correct or line=='exit'):
        print '\nYou must type a list of integers: [a, b, c, d, ...]'
        print 'What is the result of executing the following sentence?'
        print '(Type "exit" (without quotes) to exit the program)'
        print '>>> range(' + str(param[0]) + ', ' + str(param[1]) + ', ' + str(param[2]) + ')'
        line = raw_input()
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

    if (line==resul):
        return 1
    else:
        return -1


def ex3_ant(resuelto):
    if (resuelto):
        return -3

    pattern = re.compile("^[a-zA-Z0-9]+[a-zA-Z0-9_]*$")

    print 'Write a valid Python identifier that includes at least:'
    print ' - A number'
    print ' - A letter'
    print ' - A non-alphanumeric symbol'
    print '(Type "exit" (without quotes) to exit the program)'
    identifier = raw_input('')

    if (identifier=='exit'):
        return -2

    if pattern.match(identifier):
        containsLetter = False
        containsDigit = False
        containsUnderscore = False
        for i in range(len(identifier)):
            if (identifier[i].isalpha()):
                containsLetter = True
            if (identifier[i].isdigit()):
                containsDigit = True
            if (identifier[i]=='_'):
                containsUnderscore = True
        if (containsLetter and containsDigit and containsUnderscore):
            return 1
        else:
            return -1
    else:
        return -1


def ex4_ant_params():
    return random.choice('abcdefgh')

def ex4_ant(resuelto):
    column = ex4_ant_params()
    if (resuelto):
        return -3

    print 'Consider column ' + column + ' of a chessboard as fixed. If variable "row" ',
    print '(without quotes) contains the row number, replace the ellipsis in the following ',
    print 'line of code that assigns to the variable isWhite if the cell is white or not:'
    print '>>> isWhite = ...'
    print '\nBe careful to name the variable exactly as "row" (without quotes)!'
    print '(Type "exit" (without quotes) to exit the program)'
    line = raw_input('isWhite = ')

    if (line=='exit'):
        return -2

    for row in range(1,9):
        try:
            isWhite = eval(line)
            if isWhite!=((row%2)==(ord(column)+1)%2):
                return -1
        except:
            return -1

    return 1
