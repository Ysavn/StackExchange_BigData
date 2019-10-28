#!/bin/bash
#Filters the tables not needed for analysis

prefix="../StackExchangeExtracted/"
for dir in `ls $prefix`; do
    dir_loc="$prefix$dir"
    for file in `ls $dir_loc`; do
	    if [[ $file == 'PostHistory.xml' ]] || [[ $file == 'PostLinks.xml' ]];
	    then
		    eval 'rm "$dir_loc/$file"' 
	    fi
    done
done
