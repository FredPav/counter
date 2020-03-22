#!/usr/bin/env python

import sys
import re
import string

def counter(file):
    file = open(file,'r').read().split()
    d = {}
    for word in file:
        word = string.lower(word)
        pattern = re.compile('\W')
        word = re.sub('\d','',re.sub('\W', '', word))
        if word != "":
            if word in d.keys():
                d[word]+=1
            else:
                d[word]=1
    return d

def printCsv(d):
    for a in d.keys():
        print(str(a)+","+str(d[a])+",")

if __name__ == "__main__":
    printCsv(counter(sys.argv[1]))
