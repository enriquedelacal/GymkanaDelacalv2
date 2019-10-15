

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

import os.path
import glob
import sys
import random
import hashlib
import time
import re
import datetime

#modulos de cada profesor
#from jose import *
from antonio_P2_ENG import *
from brl_P2_ENG import *
from gcm_P2_ENG import *
from jose_P2_ENG import *
from noelia_P2_ENG import *


def register():
    uo_number = raw_input('Type your UO number (format: UOxxxxx): ')
    uo_number = check_uo(uo_number)
    while (uo_number==''):
        uo_number = raw_input('Wrong UO number format.\nType your UO number (format: UOxxxxx): ')
        uo_number = check_uo(uo_number)

    if (os.path.exists(uo_number + '.txt')):
        print 'The user already exists.'
        print 'If you have forgotten your password, please ask the teacher to remind it to you.'
        return ''

    print 'Your password is ' + hashlib.md5(uo_number.encode()).hexdigest()[:5]
    print 'Please, write it down.'

    user_file = open(uo_number+'.txt', 'w')
    user_file.close()

    return uo_number


def check_uo(uo_number):
    l = len(uo_number)
    if (uo_number[0]!='U' and uo_number[0]!='u'):
        return ''
    if (uo_number[1]!='O' and uo_number[1]!='o'):
        return ''
    if (not uo_number[2:].isdigit()):
        return ''
    return 'UO'+uo_number[2:]


def parse_file(filename):
    solved_ex = 0
    user_file = open(filename, 'r')
    line = user_file.readline()
    while (line != ''):
        solved_ex += int(line)
        line = user_file.readline()
    user_file.close()
    return solved_ex


def calculate_results():
    files = glob.glob('./UO*.txt')
    for f_name in files:
        score = 0.0
        f = open(f_name, 'r')
        for line in f.read().splitlines():
            trials = len(line)
            if (line[-1]=='1'):
                score = score + 1.0/trials
        if (f_name!='./UO0000.txt'):
            print(f_name[2:10] + ';' + str(score))
        else:
            print('UO0000;' + str(score))
        f.close()


def calculate_single_result(user):
    score = 0.0
    f = open(user+'.txt', 'r')
    for line in f.read().splitlines():
        trials = len(line)
        if (line[-1]=='1'):
            score = score + 1.0/trials
    return score


def check_result(result, user_file):
    if (result>0):
        time.sleep(0.85)
        print 'Correct, well done!'
        user_file.write('1\n')
        time.sleep(0.85)
        print 'Loading next exercise',
        sys.stdout.flush()
        time.sleep(0.85)
        for i in range(3):
            print '.',
            sys.stdout.flush()
            time.sleep(0.85)
        print '\n\n\n',
    elif (result==-1):
        time.sleep(0.85)
        print 'Sorry, your solution is not correct.'
        user_file.write('0')
        time.sleep(3)
        print '\n\n\n'
    elif (result==-2):
        time.sleep(0.85)
        print 'Bye!'
        time.sleep(3)
        print '\n'


def check_deadline_finished():
    deadline = time.strptime("14/12/2018 22:00", '%d/%m/%Y %H:%M')
    current_time = time.localtime()
    return time.mktime(current_time) > time.mktime(deadline)


def finished():
    print 'Sorry, the gymkhana has already finished.'



def main():
    if (check_deadline_finished()):
        finished()
        time.sleep(3)
        return

    uo_number = raw_input('Type your UO number (format: UOxxxxx): ')
    if (uo_number.lower()=='register'):
        uo_number = register()

    if (uo_number.lower()=='prof_results'):
        calculate_results()
        raw_input('Press enter to finish...')
        time.sleep(1)
        return

    if (uo_number==''):
        return

    uo_number = check_uo(uo_number)
    while (uo_number==''):
        uo_number = raw_input('Wrong UO number format.\nType your UO number (format: UOxxxxx): ')
        uo_number = check_uo(uo_number)

    if not (os.path.exists(uo_number + '.txt')):
        print 'User does not exist.'
        time.sleep(2)
        return

    uo_pass = hashlib.md5(uo_number.encode()).hexdigest()[:5]

    if (uo_number!='UO0000'):
        raw_input_pass = raw_input('Type your password: ')
        if (uo_pass != raw_input_pass):
            print 'Incorrect user and/or password'
            return

    solved_ex = parse_file(uo_number+'.txt')
    user_file = open(uo_number+'.txt', 'a')
    random.seed(int(uo_number[2:]))
    time.sleep(0.85)
    result = 1

    ejercicios = [ex1_ant, ex2_ant, ex3_ant, ex4_ant]  # iniciales
    ejercicios += [exB1, gcm_ex1, exN1, exN2]  # binario, operadores basicos, variables
    ejercicios += [jv_ex1, exN7, exN8, gcm_ex2, gcm_ex3, exB2]  # operadores logicos, condiciones, if-else
    ejercicios += [gcm_ex4, gcm_ex5, gcm_ex6, exB3, gcm_ex7, exB4]  # bucles
    ejercicios += [jv_ex3, jv_ex4, jv_ex5, jv_ex6, jv_ex7, jv_ex9, exN3, exN4, exB6, exB7]  # listas
    ejercicios += [jv_ex2, jv_ex8, jv_ex10, exN5, exN6, exB5, exB8]  # cadenas
    current_ex = 1

    while solved_ex < len(ejercicios) and (result != -2 and result != -1):
        result = ejercicios[solved_ex](solved_ex>=current_ex)
        check_result(result, user_file)
        solved_ex = solved_ex + (result > 0)
        current_ex = current_ex + 1

    if (solved_ex==len(ejercicios)):
        print '\nCongratulations, you have completed the Gymkhana!'
        print 'Your score is ' + str(calculate_single_result(uo_number)) + '\n'
        time.sleep(3)

if __name__ == '__main__':
    main()
