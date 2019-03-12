#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-04
Purpose: Matchy Matchy
"""

import argparse
import sys
import os
import re
import csv
from collections import Counter
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument(
    #     'positional', metavar='FILE', help='BLAST output (-outfmt 6)')
    parser.add_argument('file', metavar='FILE', help='Input file')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotations file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

    # parser.add_argument(
    #     '-s',
    #     '--sep',
    #     help='Field separator',
    #     metavar='str',
    #     type=str,
    #     default='')

    # parser.add_argument(
    #     '-f',
    #     '--field_names',
    #     help='Field names (no header)',
    #     metavar='str',
    #     type=str,
    #     default='qseqid, sseqid, pident, length, mismatch, gapopen, qstart, sstart, send, evalue, bitscore')

    # parser.add_argument(
    #     '-l',
    #     '--limit',
    #     help='How many records to show',
    #     metavar='int',
    #     type=int,
    #     default=1)

    # parser.add_argument(
    #     '-d',
    #     '--dense',
    #     help='Not sparse (skip empty fields)',
    #     action='store_true')

    # parser.add_argument(
    #     '-n',
    #     '--number',
    #     help='Show field number (e.g., for awk)',
    #     action='store_true')

    # parser.add_argument(
    #     '-N',
    #     '--no_headers',
    #     help='No headers in first row',
    #     action='store_true')

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

#---------------------------------------------------
def blastcheck(output):
    """runs blast check on the blast output files"""

    args = get_args()
    file = args.file
    limit = args.limit
    sep = args.sep
    dense = args.dense
    show_numbers = args.number
    no_headers = args.no_headers

    if not os.path.isfile(file):
        print('"{}" is not a file'.format(file))
        sys.exit(1)

    if not sep:
        _, ext = os.path.splitext(file)
        if ext == '.csv':
            sep = ','
        else:
            sep = '\t'

    with open(file) as csvfile:
        dict_args = {'delimiter': sep}

        if args.field_names:
            regex = re.compile(r'\s*,\s*')
            names = regex.split(args.field_names)
            if names:
                dict_args['fieldnames'] = names

        if args.no_headers:
            num_flds = len(csvfile.readline().split(sep))
            dict_args['fieldnames'] = list(
                map(lambda i: 'Field' + str(i), range(1, num_flds + 1)))
            csvfile.seek(0)

        reader = csv.DictReader(csvfile, **dict_args)
        print(reader)
        for i, row in enumerate(reader, start=1):
            vals = dict(
                [x for x in row.items() if x[1] != '']) if dense else row
            flds = vals.keys()
            longest = max(map(len, flds))
            fmt = '{:' + str(longest + 1) + '}: {}'
            print('// ****** Record {} ****** //'.format(i))
            n = 0
            for key, val in vals.items():
                n += 1
                show = fmt.format(key, val)
                if show_numbers:
                    print('{:3} {}'.format(n, show))
                else:
                    print(show)

            if i == limit:
                break

# --------------------------------------------------
def main():
    """"""
    args = get_args()
    file = args.file
    anno_file = args.annotations
    out_file = args.outfile


    # print(file)
    # print(out_file)
    # blastcheck(file)

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))
    """Cant use both of these for some reason"""
    # if not os.path.isfile(anno_file):
    #     die('"{}" is not a file'.format(anno_file)


    """Outputs the SEQID AND PIDENT OF HITS FILE
       no tested method can add to the dictionary"""
    for line in open(file):
        split = line.split('\t', 3)
        blast_seqid = split[1]
        blast_pident = split[2]
        d_blast = ({blast_seqid:blast_pident})
    # print(d_blast)
    """Chunk Status: Reads the CSV outputs a 
        bunch of ordered dicts. """
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            anno_seqid = row.get('centroid')
            anno_genus = row.get('genus')
            anno_species = row.get('species')





            # for line in open(file):
            #     split = line.split('\t', 3)
            #     blast_seqid = split[1]
            #     blast_pident = split[2]
            #     print(row)
                # d_blast = {blast_seqid: blast_pident}
                # print(blast_seqid)
                # print(blast_pident)
                # anno_seqid = row.get('centroid')
                #     if blast_seqid == anno_seqid:
                #         print('"{}" has a match'.format(blast_seqid)) 
                #     else:
                #         print('Cannot find seq "{}" in lookup'.format(blast_seqid))
                # if row.get('genus') == re.search('uncultured*', str):
                #     print('N/A')
                    # print(row.get('genus'))
                    # print(row.get('species'))

    # ATTEMPT AT USING DICT WRITER DOESNT WORK
    # with open(anno_file, 'w', newline='') as csvfile:
    #     fieldnames = ['centroid', 'domain', 'kingdom', 'phylum', 'class', 'order', 'genus', 'species']
    #     writer = csv.DictWriter(csv, fieldnames=fieldnames)
    #     # writer.writeheader()
    #     # writer.writerow({'centriod': 'genus'})
    #     # print(writer)"""
# --------------------------------------------------
if __name__ == '__main__':
    main()
