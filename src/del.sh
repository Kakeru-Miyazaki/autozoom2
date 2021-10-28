#!/bin/bash
cd ~/autozoom2/src
cat -n data.txt
echo tell me the number you want to delete
read input
expr "$input" + 1 >&/dev/null
ret=$?
if [ $? -lt 2 ];then
  python3 del.py $input > datatmp.txt
  grep -v -e '^\s*#' -e '^\s*$' datatmp.txt > data.txt
  rm datatmp.txt
  echo your meeting list is below
  cat -n data.txt
else
  echo "$input is not a number"
fi