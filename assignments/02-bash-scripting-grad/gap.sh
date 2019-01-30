#!/usr/bin/env bash

####this is gap.sh####
#### prints countries in the file gapminder ####

#### Usage statement

if [[ $# -eq "--help" ]]; then
        echo "Usage: gap.sh [SEARCH_TERMS]"
        exit 1
fi

#### Variable Assignment
SEARCH_TERMS=$1

#### temporary file for manipulating search results
mktemp FILES_LIST.tmp.XXX -q

#### Output files contents into temp file
ls ../../data/gapminder > FILES_LIST.tmp.*

#### Sort and filter list of countries according to 
grep -i -w I* FILES_LIST.tmp.*

cat FILES_LIST.tmp.*

#### Removing the temp file
rm FILES_LIST.tmp.*


