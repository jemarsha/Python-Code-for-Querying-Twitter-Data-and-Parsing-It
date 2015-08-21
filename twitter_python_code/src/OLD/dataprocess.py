#!/usr/bin/env python
import json


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def main( mode = 1 ):

    with open('./datatmp/tmp.json') as f:

#        content = f.splitlines()
        for c in nonblank_lines(f):
            
            
            e = c.strip()

            if e is not None:
                d = json.loads(e)
                print(d['text'])

if __name__ == '__main__':
    main()

