####this is cat-n.sh####
####it mimics the output of the command cat -n ####

#!/c/Users/Donald

#### If there are no arguments it should print a Usage Statement and
#### exit with an error code (greater than zero)

if [[ $# -eq 0 ]]; then
	echo "Usage: cat-n.sh ARG"
	exit 1
fi

#### Program will expect to recieve an argument in $1

ARG=$1

#### If the argument is not a file it should notify the user and exit with
#### a different error code

if [[ ! -f "$ARG" ]]; then
        echo "ARG is NOT a file"
	exit 2
fi

#### It will iterate over the lines in the files and print
######## the line number, a space , and line from the file
i=0
FILE=$1
while read -r LINE; do
	i=$((i+1))
	echo $i $LINE
done < "$FILE"

