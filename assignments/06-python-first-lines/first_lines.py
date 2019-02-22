#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-19
Purpose: Skim a bunch of poems
"""

import re
import os
import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-w',
        '--int',
        help='Number of characters per line?',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        'directory', metavar='DIR', help='Chosen directory', nargs='+')

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

#### Perhaps a function to reuse my head program?

# --------------------------------------------------
def main():
    """TOoT toOT tOOt TooT
        tots jazz noises
         that trombone.    """

    args = get_args()
    width = args.int
#    dots = '.'*int
    #### Error message for not a directory
    for dirname in args.directory:
       if not os.path.isdir(dirname):
          warn('"{}" is not a directory'.format(dirname))
          continue

       d = {}
# d[line] = file
#sorted(d.items)
       print(dirname)
       #### creating variables
       for file in os.listdir(dirname):
           path = os.path.join(dirname, file)
           line = open(path).readline().rstrip()
           d[line] = file

       for line, file in sorted(d.items()):
           linew = len(line)
           filew = len(file)
           dots = '.'*(width - linew - filew)

           print('{} {} {}'.format(line, dots, file))
####Maybe did it wrong, again
"""           for key in d:
              keyw = len(key)
              filew = len(file)
              dots = '.'*(width - keyw - filew)
           
           print('{}{}{}'.format(key, dots, file))

"""




       #### HOARD ALL THE CODE
"""    for file in os.listdir(dirname):
       filelocation = dirname + '/' + file
       with open(filelocation) as poem:
          for line in poem:

          d = {'line': (line), 'ellipse': (dots), 'file': (path)}
          print(d.get('line'),end='')
          print(d.get('ellipse'))
          print(d.get('file'))
          #print('{} {}'.format(d.get('line'), (d.get('ellipse'))
"""

       #### old code I am hoarding just in case
"""    for file in os.listdir(dirname):
       print('.'*int + ' {}'.format(file))
       filelocation = dirname + '/' + file
       with open(filelocation) as poem:
          for line in poem:
             #print('{} {} {}'.format(line, dots, file), end='')
             print('{} '.format(line) + ' {} '.format(dots) + ' {}'.format(dots), end='')
"""


# --------------------------------------------------
if __name__ == '__main__':
    main()
