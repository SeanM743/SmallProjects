# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:13:13 2019

@author: snama
"""

import string, re
import itertools


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    
    for p in fill_in(formula):
        if valid(p):
            return p
    
    return False
    
def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."
    
    letters = set([ltr for ltr in formula if ltr in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    letters = ''.join(letters)
    
    for perm in itertools.permutations('1234567890',len(letters)):
        st = formula.maketrans(letters,''.join(perm))
        yield formula.translate(st)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False