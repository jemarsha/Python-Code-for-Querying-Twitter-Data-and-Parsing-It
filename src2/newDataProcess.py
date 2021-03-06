#!/usr/bin/env python
import sys, getopt
import json
import random
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
        opts, args = getopt.getopt(argv,"hi:o:w:",['ifile','ofile','wfile'])
    except getopt.GetoptError:
        print 'newDataProcess.py -i <inputfile> -o <outputfile> -w <wordfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'newDataProcess.py -i <inputfile> -o <outputfile> -w <wordfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-w", "--wfile"):
            wordfile = arg

    d = {}
    wd = {}
    violentAu = []
    nonViolentAu = []
    totCount = 0
    allCount = 0
    with open(wordfile,'r') as fword:
        for c in nonblank_lines(fword):
            e = c.strip()
            #print(e)
            wd[e] = 0
           #print(e,wd[e])
 
    with open(inputfile,'r') as fin:
        
            for c in nonblank_lines(fin):
                #formatting tweets and get author and tweet text
                e = c.strip()
                if e is not None:
                    d = json.loads(e)                    
                    author=d['user']['id_str']
                    text=d['text']
                    lang=d['user']['lang']

                    if lang == 'en':
                        print (lang)
                        print (text)
                        print (author)
                        #violentAu.extend(author)


                        ctext = text.strip()
                        words = ctext.split()
                        wordFound=0
                         
                        for word in words:
                            count = wd.get(word)
                            allCount= allCount+1
                            
                            #            print(word,count)
                            if count is not None:
                                wordFound=1
                                totCount = totCount +1
                                wd[word] = count+1
                        if wordFound==1:
                            violentAu.append(author)
                        else:
                            nonViolentAu.append(author)
                        
    nva= random.sample(range(len(nonViolentAu)), len(violentAu))
    print(len(nonViolentAu))
    print(len(violentAu))
    print(nva)
    print(violentAu)
    print(nonViolentAu)
    nv_outputfile = outputfile+'_nv'
    v_outputfile = outputfile+'_v'
    wcount_outputfile = outputfile+'_wcount'
    tcount_outputfile = outputfile+'_tcount'


    with open(nv_outputfile,'w') as fout:
        for i in range(0, len(nva)):
            fout.write(nonViolentAu[nva[i]]+"\n")
    
    with open(v_outputfile,'w') as fout:
        for i in range(0, len(nva)):
            fout.write(violentAu[i]+ "\n")

    with open(wcount_outputfile, 'w') as fout:
        fout.write(str(totCount))

    with open(tcount_outputfile, 'w') as fout:
        fout.write(str(allCount))


if __name__ == '__main__':
    main(sys.argv[1:])

#  with open(outputfile,'w') as fout:
