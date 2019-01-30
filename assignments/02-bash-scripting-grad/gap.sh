#!/usr/bin/env bash

####this is gap.sh####
#### prints countries in the directory gapminder ####

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
TMP_FILE=$(mktemp)
TMP_SORTED=$(mktemp)

#### Output files contents into temp file
ls ../../data/gapminder > $TMP_FILE

#### Sort and filter list of countries according to user input
grep -i "^$SEARCH_TERMS" $TMP_FILE > $TMP_SORTED

#### remove .cc.txt
cat $TMP_SORTED | cut -d '.' -f 1




