#!/bin/bash
cd ~/autozoom2/src
now=`date +"%a %H%M"`
url=`python3 main.py $now` && open $url
if test $? -eq 1; then
echo You have no meeting today.
fi

# sleep 30