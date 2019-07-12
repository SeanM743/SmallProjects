# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:02:16 2019

@author: snama
"""
#develop an n_ary function to take a binary and return an n_ary function handle

from functools import update_wrapper

#def n_ary(f):
#    """Given binary function f(x, y), return an n_ary function such
#    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
#    def n_ary_f(x, *args):
#        return x if not args else f(x,n_ary_f(*args))
#    update_wrapper(n_ary_f,f) #allows help() to display correct function name
#    return n_ary_f

# @n_ary  decorator function
def seq(x,y): return ('seq',x,y)
#seq = n_ary(seq) is same as using decorator function @n_ary

#update wrapper makes us repeat ourselves

def decorator(d):
    
    "Make function d a doecorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn),fn)
    update_wrapper(_d,d)
    return _d

@decorator
def n_ary(f):
    def n_ary_f(x,*args):
        return x if not args else f(x,n_ary_f(*args))
    return n_ary_f

