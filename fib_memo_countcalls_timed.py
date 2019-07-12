# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:29:40 2019

@author: snama
"""

from functools import update_wrapper

def decorator(d):
    
    def _d(fn):
        return update_wrapper(d(fn),fn)
    update_wrapper(_d,d)
    return _d

def memo(f):
    cache = {}
    
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return cache[args]
        except TypeError:
            return f(args)
    return _f

#Making a callcounts dictionary to count the number of function calls
@decorator
def countcalls(f):

    def _f(*args):
        try:
            c[_f] += 1
            return f(*args)
        except KeyError:
            c[_f]= 1
            return f(*args)
    c[_f] = 0
    return _f
        
c = {}

@countcalls
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2) 

                