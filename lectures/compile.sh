#!/usr/bin/env bash

TMP=$(mktemp)

i=0
for MD in $(find . -name \*.md | sort); do
    i=$((i+1))
    printf "%3d: %s\n" $i $MD

    if [[ $i -gt 1 ]]; then
        echo '' >> "$TMP"
        echo '\pagebreak' >> "$TMP"
        echo '' >> "$TMP"
    fi

    cat "$MD" >> "$TMP"
done

for EXT in epub pdf; do
    echo "Producing $EXT"
    pandoc -F ../bin/include.hs "$TMP" -o "biosys.$EXT"
done

rm "$TMP"
echo "Done."
