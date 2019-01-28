####this is head.sh####
####it mimics the output of the command head####

#!/c/Users/Donald

#### If there are no arguments it should print a Usage Statement and
#### exit with an error code (greater than zero)

if [[ $# -eq 0 ]]; then
	echo "Usage: head.sh ARG LINES"
	exit 1
fi

#### Program will expect to recieve an argument in $1 and maybe in $2

ARG=$1
LINE=${2:-3}

#### If the argument is not a file it should notify the user and exit with
#### a different error code

if [[ ! -f "$ARG" ]]; then
        echo "ARG is NOT a file"
	exit 2
fi

#### print the number of lines requested by the user by iterating over
#### the lines in the file and exiting the loop appropiately

i=0
FILE=$1
while read -r LINE; do
	i=$((i+1))
	if [[ $i -eq $2 ]]; then
		break
	fi
	echo $i $LINE
done < "$FILE"
