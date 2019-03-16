#!/usr/bin/env bash

#### hello.sh ####
#### a friendly greeting ####

#### if no args print a usage statement, exit with error code
if [[ $# -eq 0 ]]; then
        echo "Usage: hello.sh GREETING [NAME]"
        exit 1
fi

#### if more than 2 args print usage, exit with error code
if [[ $# -gt 2 ]]; then
        echo "Usage: hello.sh GREETING [NAME]"
        exit 2
fi

#### $1 is a greeting, $2 is an optional title with Human as default

GREETING=$1
NAME=${2:-"Human"}

#### print the greeting, a comma and space, the name and an !

echo "$GREETING"", ""$NAME""!"

