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
    print('Usage: vowel_counter.py STRING')
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

if count == 0:
    print('There are ' + str(count) + ' vowels in \"' + str(word) + '.\"')
elif count == 1:
    print('There is ' + str(count) + ' vowel in \"' + str(word) + '.\"')
elif count > 1:
    print('There are ' + str(count) + ' vowels in \"' + str(word) + '.\"')

#---------------------------------------------------
