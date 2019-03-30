#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-02
Purpose: Rock the Casbah
"""

import os
import sys
import re

args = sys.argv[1:]

#-------------------------------------------------

if len(args) != 1:
    print('Usage: dates.py "STRING of dates"')
    sys.exit(1)

""" These should fit in all one regex
2012-03-09T08:59
2012-03-09T08:59:03
2017-06-16Z
2015-01
2015-01/2015-02
2015-01-03/2015-02-14
2017-06-16Z
20100910 Might fit here with some effort
"""

arg = args[0]

date_re = re.compile('(?P<year>\d{4})'     # YYYY
                     '[/-]?'               # optional seperator
                     '(?P<month>\d{2})'    # MM
                     '[-]?'               # optional seperator
                     '(?P<day>\d{2})?')     # DD

date_re2 = re.compile('(?P<year>\d{2})'
                       '[/-]?'
                       '(?P<month>\d{2})')

match = date_re.match(arg) or date_re2.match(arg)

d_match = (match.groupdict())

if match == None:
    print('No match')
    sys.exit(0)

if len(d_match) < 3:
    d_match['day'] = '01'

print('{}-{}-{}'.format(d_match.get('year'), d_match.get('month'), d_match.get('day')))


""" These might be a seperate regex
12/06
2/14
2/14-12/15
"""

""" Another Regex
Dec-2015
Dec, 2015
March-2017
April, 2017
"""

# OLD CODE HOARDING

# parts = {'year': match.group('year'), 
#          'month': match.group('month'),
#          'day': match.group('day')}

# print(parts)

# if parts[2] == None:
#     parts[2] = '01'

# print('{}-{}-{}'.format(parts[0], 
#                         parts[1],
#                         parts[2]))


# OLD FORMAT BEING HOARDED
# standard = '{}-{}-{}'.format(match1.group('year'),
#                              match1.group('month'),
#                              match1.group('day'))
