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

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state
    print(args)
#### STATE ERROR MESSAGES
    count = 0
    ### state too big
    if len(state) > 9:
       print('State "{}" must be 9 characters of only ., X, O'.format(state))
       sys.exit(1)
    #### state too small
    if len(state) < 9:
       print('State "{}" must be 9 characters of only ., X, O'.format(state))
       sys.exit(1)
    ### Cause I spent too long trying to use regular expressions.
    for character in state:
       if character == 'X':
          count += 1
       if character == 'O':
          count += 1
       if character == '.':
          count += 1
    if count != 9:
       print('State "{}" must be 9 characters of only ., X, O'.format(state))
       sys.exit(1)

##### CELL ERROR MESSAGES
  #  cell = args.cell
 #   player = args.player
#
#    if cell > 9:
    #   print('Invalid cell "{}", must be 1-9'.format(cell))
   #    sys.exit(1)
  #  if cell < 1:
 #      print('Invalid cell "{}", must be 1-9'.format(cell))
#       sys.exit(1)

##### PLAYER ERROR MESSAGES
#    player = args.player
#    while player == 'X':
 #      print('X is good')
  #  else player == 'O':
   #    print('O is good')

##### CELL ERROR MESSAGES
#    cell = args.cell
 #   for cell in range(0-10):
  #     print('Another type')


  #  print(state)
 #   print(player)
#    print(cell)


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
