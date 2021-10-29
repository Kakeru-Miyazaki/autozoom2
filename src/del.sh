#!/bin/bash
python3 del.py > datatmp.txt
# python3 del.py $input > datatmp.txt
grep -v -e '^\s*#' -e '^\s*$' datatmp.txt > data.txt
sort data.txt > datatmp.txt
mv datatmp.txt data.txt
bash autozoom2