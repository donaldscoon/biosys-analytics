#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    items =[]

    while(True):
        item = input('What are you bringing? ["quit" to quit]')
        items.append(item)
        if item == 'quit':
              break
        print('You are bringing {}.'.format(items))

    print('Done')


# --------------------------------------------------
main()
