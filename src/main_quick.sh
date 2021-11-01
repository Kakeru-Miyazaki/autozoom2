#!/bin/bash
cd ~/autozoom2/src
now=`date +"%a %H%M"`
if [ "$(uname)" == 'Darwin' ]; then
  # "Mac"
  url=`python3 main.py $now` && open $url
  if test $? -eq 1; then
    python3 nomeeting.py
  fi
elif [ "$(expr substr $(uname -s) 1 5)" == 'Linux' ]; then
  # "Linux"
  url=`python3 main.py $now` && xdg-open $url
  if test $? -eq 1; then
    python3 nomeeting.py
    bash autozoom2
  fi
  sleep 5
fi