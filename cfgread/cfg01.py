#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    for line in configfile:
        print(line.strip(), end=',')
        
## file was just auto closed (no more indenting)
print()
## each item of the list now has the "\n" characters back
#print(configlist)

