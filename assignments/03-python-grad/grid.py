#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-04
Purpose: Make a pretty number grid
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    

    if len(args) != 1:
        print('Usage: grid.py NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    grid_size = int(args[0])

    if (grid_size) < 2:
        print('NUM (' + str((grid_size)) + ') must be between 1 and 9')
        sys.exit(1)
    if (grid_size) > 9:
        print('NUM (' + str((grid_size)) + ') must be between 1 and 9')
        sys.exit(1)
    
# ----------------------------------------------------------------------------
#### grid sizes
    
    count = 0

    if (grid_size) == 2:
        final = 4
        rows = 2
    if (grid_size) == 3:
        final = 9
        rows = 3
    if (grid_size) == 4:
        final = 16
        rows = 4
    if (grid_size) == 5:
        final = 25
        rows = 5
    if (grid_size) == 6:
        final = 36
        rows = 6
    if (grid_size) == 7:
        final = 42
        rows = 7
    if (grid_size) == 8:
        final = 64
        rows = 8
    if (grid_size) == 9:
        final = 81
        rows = 9

    print(final)
    print(rows)

#### perhaps similar structure to hello print, but with rows?
#### curly brackets can be used to call lists
    
    testgrid = [1, 2, 3, 4]
    print(testgrid[:2])
    print(testgrid[2:])



# --------------------------------------------------
main() 

""" 
names = ['Larry', 'Moe', 'Curly', 'Shemp'

for name in names:
	print(i + 1, name)
	i += 1
 
for i, name in enumerate(names):   #### gives position and name useful for later hw
	print(i + 1, name)


"""
"""
num = 2
num ** 2
range(num ** 2)
for i in range(num ** 2):
	print(i)

for i in range(1, num ** 2 + 1):
	print(i)

for i in range(, num ** 2 +1 ):
	print('{:3}'.format(i), end='')
"""
