
#!/usr/bin/env bash

####this is gap.sh####
#### prints countries in the directory gapminder ####

#### Usage statement

if [[ $# -gt 1 ]]; then
        echo "Usage: gap.sh SEARCH_TERMS"
        exit 1
fi

#### Variable Assignment
SEARCH_TERMS=$1
TMP_FILE=$(mktemp)
TMP_SORTED=$(mktemp)

#### Output files contents into temp file
ls ../../data/gapminder > $TMP_FILE

#### Sort and filter list of countries according to user input
grep -i "^$SEARCH_TERMS" $TMP_FILE > $TMP_SORTED

NUM_FILES=$(wc -l "$TMP_SORTED" |awk '{print $1}')

if [[ $NUM_FILES -lt 1 ]]; then
      echo "There are no countries starting with \"$SEARCH_TERMS\""
      exit 0
fi

#### remove .cc.txt
cat $TMP_SORTED | cut -d '.' -f 1

