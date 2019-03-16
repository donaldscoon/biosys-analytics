#!/usr/bin/env bash

TMP=$(mktemp)

<<<<<<< HEAD
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
=======
cat /dev/null > "$TMP"

i=0
for MD in $(find . -maxdepth 2 -mindepth 2 -name \*.md | sort); do
    i=$((i+1))
    printf "%3d: %s\n" $i "$MD"

    echo "# Chapter $i" >> "$TMP"
    echo "" >> "$TMP"
    cat "$MD" >> "$TMP"

    echo "" >> "$TMP"
    echo '\pagebreak' >> "$TMP"
    echo "" >> "$TMP"
done

for EXT in pdf epub; do
>>>>>>> 98bb4c5d0ffaa18ac088e3e7c628e06d543758a7
    pandoc -F ../bin/include.hs "$TMP" -o "biosys.$EXT"
done

rm "$TMP"
<<<<<<< HEAD
=======

>>>>>>> 98bb4c5d0ffaa18ac088e3e7c628e06d543758a7
echo "Done."
