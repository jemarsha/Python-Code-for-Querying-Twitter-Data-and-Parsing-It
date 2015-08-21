#!/usr/bin/env python

import sys, getopt
import json
from pprint import pprint

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
        opts, args = getopt.getopt(argv,"hi:o:",['ifile','ofile',]'wfile'])
    except getopt.GetoptError:
        print 'dataprocess.py -i <inputifle> -o <outputfile> -w <wordfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'dataprocess.py -i <inputfile> -o <outputfile> -w <wordfile>' '
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-w", "--wfile");
            wordfile =arg

    d={}

    with open(wordfile,'r') as fword:
        for c in nonblank_lines(fword):
            e = c.strip()
            print(e)
            d[e] = 0
            print(e,d[e])

    with open(inputfile,'r') as fin:
        with open(outputfile,'w') as fout:
            for c in nonblank_lines(fin):
                
                e = c.strip()

                if e is not None:

                    d = json.loads(e)                    

#                    print(d['user']['id_str'])
                    author=d['user']['id_str']
                    data=['text']
                   # if 
                    fout.write(data.encode('utf8')+'\n')
if __name__ == '__main__':
    main(sys.argv[1:])

