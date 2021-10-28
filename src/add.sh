#!/bin/bash
echo "Please input the Day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)"
echo -n " >>  "
read day
echo

echo "Tell me the meeting time. (10-15 minute before of start is best.)"
echo " ex) 8:30 -> 0830, 13:07 -> 1307"
echo -n " >>  "
read time
echo

echo "Please tell me meeting name"
echo -n " >>  "
read name
echo

echo "Tell me the meeting URL"
echo -n " >>  "
read url

echo $day $time $name $url >> data.txt
echo registered 
echo $day 
echo $time 
echo $name 
echo $url
sort data.txt > datatmp.txt
mv datatmp.txt data.txt
#head -n -1 data.txt
echo
echo The followings is your list
cat data.txt
