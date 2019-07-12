# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:03:13 2019

@author: snama
"""
#match pattern against start of text and return longest match
def match(pattern,text):
    remainders = pattern(text)
    if remainders:
        shortest= min(remainders,key=len)
        return text[:len(text)-len(shortest)]

def lit(s): return (lambda text: set([text[len(s):]]) if text.startswith(s) else set([''])) 
def seq(x,y): return (lambda text: set().union(*map(y,x(text))))
def alt(x,y): return lambda text: x(text) | y(text)
def oneof(chars): return lambda text: set([text[1:]]) if (text and text[0] in chars) else set([''])
dot = lambda t: set([t[1:]]) if t else set([''])
eol = lambda t: set(['']) if t =='' else set([''])

def star(x): return lambda text: (set([text]) | set(t2 for t1 in x(text) if t1 != text 
                                  for t2 in star(x)(t1)))