#!/bin/bash

python3 add.py >> data.txt
sort data.txt > datatmp.txt
mv datatmp.txt data.txt
echo
echo The followings is your list
cat data.txt
