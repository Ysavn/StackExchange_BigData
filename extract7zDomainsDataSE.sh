#!/bin/bash

prefix_s="./SE_BD_7zFiles/"
prefix_d="./SE_BD_ExtractedFolder/"
for entry in `ls $prefix_s`; do
    dir="${entry%???}/"
    eval '7za x "$prefix_s$entry" -o"$prefix_d$dir"'
done
