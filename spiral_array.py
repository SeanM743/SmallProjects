# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:15:34 2019

@author: snama
"""

#return spiral array of 2D contents

def spiral(input):
    
    #my strategy is to go right by n-1, down by n-1, left by n-1 and up by n-1
    result = []
    n = len(input)
    
    def spiral_cw(offset):
        
        if offset == (n-offset-1): #in the center of an odd sized 2D array, add the last element
            result.append(input[offset][offset])
        
        result.extend(input[offset][offset:-1-offset])
        result.extend(list(zip(*input))[-1-offset][offset:-1-offset])
        result.extend(input[-1-offset][-1-offset:offset:-1])
        result.extend(list(zip(*input))[offset][-1-offset:offset:-1])
    
    for offset in range(0,n+1//2):
        spiral_cw(offset)
    
    return result

input = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 4],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(spiral(input))
    
    