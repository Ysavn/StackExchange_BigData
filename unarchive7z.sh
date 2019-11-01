#!/bin/bash

prefix_s="/Users/avneet/Documents/Fall-19/SE_7zFiles/"
prefix_d="/Users/avneet/Documents/Fall-19/SE_Unarchive/"
for entry in `ls $prefix_s`; do
    dir="${entry%???}/"
    echo $dir
    eval '7za x "$prefix_s$entry" -o"$prefix_d"'
done
