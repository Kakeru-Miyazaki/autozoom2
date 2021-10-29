#!/bin/bash
python3 add.py >> data.txt
sort data.txt > datatmp.txt
mv datatmp.txt data.txt
bash autozoom2