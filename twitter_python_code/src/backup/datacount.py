#!/usr/bin/env python

import sys, getopt
import json


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def main(argv):

    inputfile = 'empty path'
    outputfile = 'empty path'
    field = 'empty field'

    try:
        opts, args = getopt.getopt(argv,"hi:o:w:",['ifile','ofile','wfile'])
    except getopt.GetoptError:
        print 'datacount.py -i <inputifle> -o <outputfile> -w <wordfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'datacount.py -i <inputfile> -o <outputfile> -w <wordfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-w", "--wfile"):
            wordfile = arg

    d = {}

    with open(wordfile,'r') as fword:
        for c in nonblank_lines(fword):
            e = c.strip()
            print(e)
            d[e] = 0
            print(e,d[e])

    totCount = 0
    with open(inputfile,'r') as fin:
        for c in nonblank_lines(fin):
            text = c.strip()
            words = text.split()
            for word in words:
                count = d.get(word)
                print(word,count)
                if count is not None:
                    totCount = totCount +1
                    d[word] = count+1

    #Write out count
    with open(outputfile,'w') as fout:
        print(totCount)
        fout.write(str(totCount))
                    
if __name__ == '__main__':
    main(sys.argv[1:])

