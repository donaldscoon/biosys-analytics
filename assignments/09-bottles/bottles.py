#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-16
Purpose: Enterntain on Road Trips
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='Number of bottles in the song',
        metavar='int',
        type=int,
        default=10)

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
    """Drunken Jazz Noises"""
    args = get_args()
    bottles = args.num_bottles

    if bottles < 1:
        die('N() must be a positive integer.')
        
    while bottles > 0:
        if bottles > 1:
            print('{} bottles of beer on the wall,'.format(bottles))
            print('{} bottles of beer,'.format(bottles))
            print('Take one down, pass it around,')
            bottles -= 1
            if bottles == 1:
                print('{} bottle of beer on the wall!'.format(bottles))
                print('')
            else:
                print('{} bottles of beer on the wall!'.format(bottles))
                print('')
        elif bottles == 1:
            print('{} bottle of beer on the wall,'.format(bottles))
            print('{} bottle of beer,'.format(bottles))
            print('Take one down, pass it around,')
            bottles -= 1
            print('{} bottles of beer on the wall!'.format(bottles))
# --------------------------------------------------
if __name__ == '__main__':
    main()
