# -*- coding: utf-8 -*-
"""
@author: Gabriel Cebrián Márquez (cebriangabriel@uniovi.es)
@author: José Ramón Villar Flecha (villarjose@uniovi.es)
"""
from RestrictedPython import compile_restricted
from RestrictedPython.Eval import default_guarded_getiter
from RestrictedPython.Guards import guarded_iter_unpack_sequence
from RestrictedPython.Guards import safer_getattr

from RestrictedPython import safe_globals
from RestrictedPython import safe_builtins
from RestrictedPython import limited_builtins
from RestrictedPython import utility_builtins


global LANG

global TXT_FG_COLOR
global TXT_BG_COLOR
global TXT_FONTFACE
global TXT_END


def initialize():
    global LANG

    global TXT_FG_COLOR
    global TXT_BG_COLOR
    global TXT_FONTFACE
    global TXT_END

    LANG = 'ES_ES'

    TXT_FG_COLOR = {'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
                    'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m', 'white': '\033[37m'}
    TXT_BG_COLOR = {'black': '\033[40m', 'red': '\033[41m', 'green': '\033[42m', 'yellow': '\033[43m',
                    'blue': '\033[44m', 'magenta': '\033[45m', 'cyan': '\033[46m', 'white': '\033[47m'}
    TXT_FONTFACE = {'bold': '\033[1m', 'underline': '\033[4m'}
    TXT_END = '\033[0m'


def create_secure_dict():
    t = dict(__builtins__={**safe_globals, **limited_builtins, **utility_builtins})
    return t


def initialize_local_dict():
    t = {
        '_getiter_': default_guarded_getiter,
        '_iter_unpack_sequence_': guarded_iter_unpack_sequence,
        '_getattr_': safer_getattr
    }
    return t


def safe_getitem_str(obj, indx):
    if type(obj) is str:
        return obj[indx]
    else:
        raise Exception('safe_getitem_str: object is not a st.')


def add_getitem_str_to_local_dictionary(t):
    t['_getitem_'] = safe_getitem_str
    return t
