#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-12
Purpose: Ro Sham Bo!!!
"""

import re
import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='The state of the board',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state',
        metavar='str',
        type=str,
        default=None)

    parser.add_argument(
        '-c',
        '--cell',
        help='The cell to alter',
        metavar='int',
        type=int,
        default=None)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------ERROR MESSAGES------------------------------------
def die(msg='Something bad happened'):
    warn(msg)
    sys.exit(1)

#    args = get_args()
#    statecheck = args.state
#    print(statecheck)

#    if statecheck == 4:
#       print(statecheck)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state

    match = re.search('XO*', (state))
    print(match.group())
    #if statecheck != '.........':
     #   print('If is working')

##### Creating a grid
    print('-------------')
    for i, c in enumerate(state,start=1):
       cell_state = i if c == '.' else c
       print('| {} '.format(cell_state), end='')
       if i % 3 == 0:
          print('|')
          print('-------------')


# --------------------------------------------------
if __name__ == '__main__':
    main()
