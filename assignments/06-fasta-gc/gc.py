#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import os
import argparse
import sys
import re
from collections import Counter
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='FASTA files to read', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='directory name to write the output',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Percent GC',
        metavar='int',
        type=int,
        default=50)

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
    """Scatty Datt Dat Doo"""
    args = get_args()
    fasta = args.positional
    out_dir = args.outdir
    pct_gc = args.pct_gc

    if not 100 >= pct_gc > 0:
        die('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))


#    for file in fasta:
 #       if not os.path.isfile(file):
  #          warn('"{}" is not a file'.format(file))
   #         continue

 #   if not 100 >= pct_gc > 0:
#        die('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))

    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)


    file_count = 0
    num_written = 0

    for file in fasta:
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue
        
        file_count += 1
        split_file = (os.path.splitext(os.path.basename(file)))
        high_fh = open(out_dir + '/' + split_file[0] + '_high' + split_file[1], 'w')
        low_fh = open(out_dir + '/' + split_file[0] + '_low' + split_file[1], 'w')
        #print(high_fh)
        #print(low_fh)
        #print(split_file)
        for record in SeqIO.parse(file, 'fasta'):
            #print(record.seq)
            seq_len = len(record.seq)
            #print(seq_len)
            nucleo = (Counter(record.seq))
            #print(nucleo)
            gc_num = nucleo.get('G', 0) + nucleo.get('C', 0)
            #print(record.seq)
            gc = (int(gc_num/seq_len * 100))
            #print(gc)
            if gc >= pct_gc:
                #high_fh = ('{}_HIGH'.format(fasta[0]))
                #print('{}'.format(record.seq), file=high_file)
                SeqIO.write(record, high_fh, "fasta") #Don't know how to use

            else:
                #low_fh = ('{}_LOW'.format(fasta[0]))
                #print('{}'.format(record.seq), file=low_file)
                SeqIO.write(record, low_fh, "fasta")

            #print(gc_state)
            #print(SeqIO.write(gc, gc_state, 'fasta')
            #record_dict = {gc:gc_state}
            #print(record_dict)

#            open(gc_state, 'w')
#            print('{}'.format(record.seq), file=gc_state)
            #open(out_file)

            ##### works just enough to print only one line #####
            """with open(gc_state, 'w') as out_file:
                print('{}'.format(record.seq), file=out_file)"""


#            for items in record_dict:
#                print(record_dict[gc_state])
            num_written += 1
        high_fh.close()
        low_fh.close()
     
     if not num_written == 0:   
         print('Done, wrote {} to out dir "{}"'.format(num_written, out_dir))






#--------------------------------------------------
if __name__ == '__main__':
    main()
