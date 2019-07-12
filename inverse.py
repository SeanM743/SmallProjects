# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:09:58 2019

@author: snama
"""

def slow_inverse(f,delta = 1/1024):
    
    def _inv(y):
        x = 0
        while f(x)-delta < y:
            x+=delta
        
        return x if (f(x)-y) < (y-f(x-delta)) else (x-delta) 
    
    return _inv

def inverse(f,delta=1/1024):
        
    def _inv(y):
        x = 1
        while f(x) < y:
            x = 2*x
        low, high = 0,x
        mid = (low+high)/2
        
        while abs(y-f(mid)) > delta:
            if f(mid) > y:
                high = mid
            else:
                low = mid
            mid = (low+high)/2
        return mid
    
    return _inv

def square(x): return x*x
def pow10(x): return 10**x

a = inverse(square)
log10 = inverse(pow10)
print(log10(134))

