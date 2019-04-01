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

arg = args[0]

""" First REGEX covers these formats
2012-03-09T08:59
2012-03-09T08:59:03
2017-06-16Z
2015-01
2015-01/2015-02
2015-01-03/2015-02-14
2017-06-16Z
"""

date_re = re.compile('(?P<year>\d{4})'     # YYYY
                     '[/-]?'               # optional seperator
                     '(?P<month>\d{2})'    # MM
                     '[-]?'               # optional seperator
                     '(?P<day>\d{2})?')     # DD

""" 2nd REGEX covers
12/06
"""

date_re2 = re.compile('(?P<month>\d{1,2})'
                       '[/-]?'
                       '(?P<year>\d{2})')

""" 3rd REGEX covers
2/14
2/14-12/15
"""

date_re3 = re.compile('(?P<month>\d{1})'
                      '[/-]'
                      '(?P<year>\d{1,2})')

""" 4th REGEX covers
Dec-2015
March-2017
Dec, 2015
April, 2017
"""

# date_re4 = re.compile('(?P<month>[Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December]{3})'
#                       '[/,-]'
#                       '([\s*])?'
#                       '(?P<year>\d{4})')

# print(date_re4)
match = (date_re.match(arg)) or (date_re2.match(arg)) or (date_re3.match(arg))# or (date_re4.match(arg))
# print(match)

d_match = (match.groupdict())

if match == None:
    print('No match')
    sys.exit(0)

if len(d_match) < 3:
    d_match['day'] = '01'
    
if d_match.get('day') == None:
    d_match['day'] = '01'

if len(d_match.get('year')) < 3:
    d_match['year'] = ('20' + d_match.get('year'))

if len(d_match.get('month')) < 2:
    d_match['month'] = ('0' + d_match.get('month'))

# if d_match.get('month') == 'Jan':
#     d_match['month'] = '01'

print('{}-{}-{}'.format(d_match.get('year'), d_match.get('month'), d_match.get('day')))