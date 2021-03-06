#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-17
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'state', metavar='STATE', help='State of the board')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Some boops and beeps of a computer starting up."""
    args = get_args()
    state = args.state
    count = 0

    #### state to big
    if len(state) > 9:
       die('State "{}" must be 9 characters of only ., X, O'.format(state))

    #### state too small
    if len(state) < 9:
       die('State "{}" must be 9 characters of only ., X, O'.format(state))

    #### Cause I spent too long trying to use regular expressions.
    for character in state:
       if character == 'X':
          count += 1
       if character == 'O':
          count += 1
       if character == '.':
          count += 1
    if count != 9:
       die('State "{}" must be 9 characters of only ., X, O'.format(state))

    state_re = re.compile('(?P<state>[XXX......|...XXX...|......XXX|X..X..X..|.X..X..X.|..X..X..X|X...X...X|..X.X.X..|OOO......|...OOO...|......OOO|O..O..O..|.O..O..O.|..O..O..O|O...O...O|..O.O.O..]{9})')
    match = (state_re.match(state))

    d_match = (match.groupdict())

    x_count = 0
    o_count = 0
    for character in d_match['state']:
      if character == 'X':
         x_count += 1
      if character == 'O':
         o_count += 1

    if x_count > o_count:
       print('X has won')
    elif x_count < o_count:
       print('O has won')
    else:
       print('No winner')

# --------------------------------------------------
if __name__ == '__main__':
    main()
