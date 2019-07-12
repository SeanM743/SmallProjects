# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:26:50 2019

@author: snama
"""

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."

    if text == '': return (0,0)
    text = text.upper()
        
    lens = [grow(text,start,end) 
            for start in range(len(text)) 
            for end in (start,start+1)]
 
    return max(lens, key = lambda args: args[1]-args[0])

def grow(text,start,end):
    while start >0 and end < len(text) and text[start-1] == text[end]:
        start -= 1; end +=1
    
    return (start,end)
    

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())