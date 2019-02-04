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
    arg = int(args[0])
    
    if len(args) != 1:
        print('Usage: grid.py NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    if (arg) < 2:
        print('NUM (' + str((arg)) + ') must be between 1 and 9')
        sys.exit(1)

    arg = args[0]

    print('Arg is "{}"'.format(arg))
    print(arg)

# --------------------------------------------------
main()
