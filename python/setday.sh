#!/usr/bin/bash

day=$1

mkdir $day
cd $day
touch "$day.test" "$day.in" "$day.py"

echo -e "from sys import argv\n\nfilename = argv[1] if len(argv) > 1 else '$day.in'\n" > "$day.py"
