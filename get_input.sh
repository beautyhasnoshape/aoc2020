#!/bin/bash

if [[ $# -eq 0 ]]; then
    day=`date "+%-d"`
else
    day=${1}
fi

if [[ ${#day} -gt 1 ]]; then
    output="${day}.txt"
else
    output="0${day}.txt"
fi

input_url=https://adventofcode.com/2020/day/${day}/input
session_id=`cat ../session_id`

curl ${input_url} -X GET -H 'Cookie: session='${session_id} > ${output}

echo
cat ${output}
echo
echo "Input downloaded from ${input_url}"
