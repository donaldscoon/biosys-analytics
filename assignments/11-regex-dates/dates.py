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
                     '(?P<month>\d{1,2})'    # MM
                     '[-]?'               # optional seperator
                     '(?P<day>\d{1,2})?')     # DD

""" 2nd REGEX covers
12/06
"""

date_re2 = re.compile('(?P<month>\d{1,2})'
                       '[/-]?'
                       '(?P<year>\d{4})')

""" 3rd REGEX covers
2/14
2/14-12/15
"""

date_re3 = re.compile('(?P<month>\d{1,2})'
                      '[/-]'
                      '(?P<year>\d{1,2})')

""" 4th REGEX covers
Dec-2015
March-2017
Dec, 2015
April, 2017
"""

date_re4 = re.compile('(?P<month>[Jan|January|Feb|February|Mar|March|Apr|April|May|Jul|July|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December]{1,9})'
                      '([/,-])?'
                      '(\s*)?'
                      '(?P<year>\d{4}$)')

match = (date_re.match(arg)) or (date_re2.match(arg)) or (date_re3.match(arg)) or (date_re4.match(arg))

if match == None:
    print('No match')
    sys.exit(0)

d_match = (match.groupdict())

if len(d_match) < 3:
    d_match['day'] = '01'

if d_match.get('day') == None:
    d_match['day'] = '01'

if len(d_match.get('day')) < 2:
    d_match['day'] = '0' + d_match.get('day')

if len(d_match.get('year')) < 3:
    d_match['year'] = ('20' + d_match.get('year'))

if len(d_match.get('month')) < 2:
    d_match['month'] = ('0' + d_match.get('month'))

d_months = {'Jan': '01', 'January': '01', 'Feb': '02', 'February': '02', 'Mar': '03', 'March': '03',
            'Apr': '04', 'April': '04', 'May': '05', 'Jun': '06', 'June': '06', 
            'Jul': '07', 'July': '07', 'Aug': '08', 'August': '08', 'Sep': '09', 'September': '09',
            'Oct': '10', 'October': '10', 'Nov': '11', 'November': '11', 'Dec': '12', 'December': '12'}

for month in d_months:
    if d_match.get('month') == month:
        d_match['month'] = (d_months.get(month))

print('{}-{}-{}'.format(d_match.get('year'), d_match.get('month'), d_match.get('day')))