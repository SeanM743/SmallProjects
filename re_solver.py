# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:55:14 2019

@author: snama
"""

def search(pattern, text):
    """Return true if pattern appears anywhere in text
	   Please fill in the match(          , text) below.
	   For example, match(your_code_here, text)"""
    if pattern.startswith('^'):
        return match( pattern[1:], text) # fill this line
    else:
        return match('.*' + pattern , text) # fill this line

def match(pattern, text):
    """
    Return True if pattern appears at the start of text
    """

    if pattern == '':
        return True
    elif pattern == '$':
        return pattern == ''
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, oper, follows = pattern[0],pattern[1],pattern[2:]
        
        if oper == '*':
            return match_star(p,text,follows)
        else: #oper is ?
            if match1(p,text) and match(pattern,text[1:]):
                return True
            else:
                return match(follows,text)
    else:
         return match1(pattern[0],text) and match(pattern[1:],text[1:])
     
def match1(p,text):
    if not text: return False
    return p == '.' or p == text[0]
    
def match_star(p,text,follows):
    return (match1(p,text) and match_star(p,text[1:],follows)) or match(follows,text)
    
    
    

                
                