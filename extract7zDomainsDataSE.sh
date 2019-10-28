#!/bin/bash

prefix_s="../StackExchange7z/"
prefix_d="../StackExchangeExtracted/"
for entry in `ls $prefix_s`; do
    dir="${entry%???}/"
    eval '7za x "$prefix_s$entry" -o"$prefix_d$dir"'
done
