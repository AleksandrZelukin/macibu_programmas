#!/usr/bin/env python3
 
ROWS = 7
COLUMNS = 21
 
matrix = [ [ '*' for j in range(COLUMNS) ] for i in range(ROWS) ]
for i in range(1, ROWS - 1):
    for j in range(1, COLUMNS - 1):
        if i != (ROWS // 2) or j == 1 or j == (COLUMNS - 2):
            matrix[i][j] = ' '
 
for i in range(ROWS):
    for j in range(COLUMNS):
        print(matrix[i][j], end='')
    print()
