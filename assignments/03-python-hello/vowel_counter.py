#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-02
Purpose: Rock the Casbah
"""

import os
import sys

args = sys.argv[1:]

#-------------------------------------------------

if len(args) != 1:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

word = args[0]

count = 0

for letter in word.lower():
    if letter == 'a':
        count += 1
    elif letter == 'e':
        count += 1
    elif letter == 'i':
        count += 1
    elif letter == 'o':
        count += 1
    elif letter == 'u':
        count += 1

if count == 5:
    print(count)

#---------------------------------------------------

# --------------------------------------------------
#def main():
#    args = sys.argv[1:]
#    count = 0
#
#    if len(args) != 1:
#        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
#        sys.exit(1)
#
#    word = args[0]
#
#    for letter in word:
#        if letter == 'a' or letter == 'A':
#            count += 1
#
#    print(str('count'))
#
#
# --------------------------------------------------
#main()
