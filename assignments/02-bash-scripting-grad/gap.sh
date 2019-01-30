#!/usr/bin/env bash

####this is gap.sh####
#### prints countries in the file gapminder ####

#### Usage statement

if [[ $1 -eq "--help" ]]; then
        echo "Usage: gap.sh '[SEARCH_TERMS]'"
	echo "SEARCH_TERMS uses regular expressions"
        exit 1
fi

if [[ $# -gt 1 ]]; then
        echo "Usage: gap.sh '[SEARCH_TERMS]'"
        exit 2
fi

#### Variable Assignment
SEARCH_TERMS=$1
i=1
#### temporary file for manipulating search results
mktemp FILES_LIST.tmp.XXX -q
mktemp SEARCH_RESULTS.tmp.XXX -q

#### Output files contents into temp file
ls ../../data/gapminder > FILES_LIST.tmp.*

#### Sort and filter list of countries according to user input
grep -i "$SEARCH_TERMS" FILES_LIST.tmp.* > SEARCH_RESULTS.tmp.*

#### remove .cc.txt
cat SEARCH_RESULTS.tmp.* | cut -d '.' -f 1

#### Removing the temp files
rm *.tmp.*


