#!/bin/bash
#Filters the tables needed for analysis
prefix_s="/Users/avneet/Documents/Fall-19/SE_Unarchive/"
prefix_d="/Users/avneet/Documents/Fall-19/SE_FilterXML/"
for dir in `ls $prefix_s`; do
    dir_loc="$prefix_s$dir"
    eval 'mkdir -p $prefix_d$dir'
    for file in `ls $dir_loc`; do
	    if [[ $file == 'Users.xml' ]] || [[ $file == 'Comments.xml' ]] || [[ $file == 'Badges.xml' ]];
	    then
		    eval 'cp $dir_loc/$file $prefix_d$dir/' 
	    fi
    done
done
