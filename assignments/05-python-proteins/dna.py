#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    DNA = args[0]

    print('DNA is "{}"'.format(DNA))

    counts = {}   #making a dictionary
    for char in DNA:
       print(char)
       if char not in counts:
          counts[char] == 0

       counts[char] += 1

    print('A = {}'.format(counts.get('A', 0)))   # safe way to extract from dictionary


# --------------------------------------------------
main()
