#!/usr/bin/env python3

"""
Author:Donald Coon
Date:02-1-19
Purpose: A warm friendly greeting.
"""

import sys
import os

#---------------------------------------------------------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME ...]').format(os.path.basename(sys.argv[0]))
        sys.exit(1)

    if len(names) == 1:
        print('Hello to the 1 of you ' + names[0] + '!')
        #print('Hello to the 1 of you: {}!'.format(names[0]))
    elif len(names) == 2:
        print('Hello to the 2 of you {}!')#.format(', and '.join(names)))
    elif len(names) == 3:
        print('Hello to the 3 of you {}!')#.format(', and '.join(names)))

#-------------------------------------------------------------------------------------------

main()
