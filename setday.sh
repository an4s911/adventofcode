#!/usr/bin/bash

lang=$1
day=$2

mkdir "$lang/$day"
cd "$lang/$day"
touch "$day.test" "$day.in" "$day.py"
