# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]  

def check_sud(input):
    
    size = len(input)
    gridsize = int(math.sqrt(9))
    
    def has_duplicate(block):
        removed_zeros = list(filter(lambda x: x != 0,block)) 
        return not len(set(removed_zeros)) == len(removed_zeros)
        
    rows = any([has_duplicate(x) for x in input])
    cols = any([has_duplicate(x) for x in 
                [[input[i][j] for i in range(size)] for j in range(size)]])
    
    grids = any([has_duplicate(x) for x in 
             list([input[i][j] for i in range(I*gridsize,gridsize*(I+1)) for j in range(J*gridsize,(J+1)*gridsize)] for I in range(gridsize) for J in range(gridsize))])
    
    return not (rows or cols or grids)

print(check_sud(input))