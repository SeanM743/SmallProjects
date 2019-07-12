# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:59:30 2019

@author: snama
"""

import itertools
import time

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def timedcall(fn,*args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0,result

def timedcalls(n,fn,*args):
    t = []
    if isinstance(n,int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        while(sum(t) < n):
            t.append(timedcall(fn,*args)[0])
    return times








