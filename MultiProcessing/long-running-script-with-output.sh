#!/bin/bash -e

FILE=${1:-results.txt}

echo "This script is the best!"

echo "Outputting results to ${FILE}"

echo "date,result_0,result_1" &> ${FILE}
for i in {1..10}; do
    echo "$(date +%FT%T),${RANDOM},${RANDOM}" &>> ${FILE}
    sleep 1
done

echo "I'm all done!"
