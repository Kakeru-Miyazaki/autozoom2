#!/bin/bash
cd ~/autozoom2/src
now=`date +"%a %H%M"`
url=`python3 main.py $now` && open $url
if test $? -eq 1; then
python3 nomeeting.py
bash autozoom2
fi