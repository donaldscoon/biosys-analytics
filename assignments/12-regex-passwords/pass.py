#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-04
Purpose: Hack passwords
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
        'password', metavar='str', help='The stored password')

    parser.add_argument(
        'entry', metavar='str', help='What the user actually inputed')

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
    """Make a jazz noise here"""
    args = get_args()
    password = args.password
    entry = args.entry.lower()

    print(password)
    print(entry)

    pass_re1 = re.compile('[^.]?'           #begining of word extra character
                          '(?P<pass>\w+)'
                          '[$.]?')           #end of word extra character

    match = pass_re1.match(entry)

    print(match)

    if password == entry:
        print('BORING')
    elif entry != None:
        print('lucky you')

# --------------------------------------------------
if __name__ == '__main__':
    main()
