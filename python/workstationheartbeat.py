
import sys
import getopt
import os
import csv

inputfile = ''
outputfile = ''
filterstr = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:", ["ifile=", "ofile=", "filter="])
    print('argv = ', sys.argv)
    print('opts = ', opts)
except getopt.GetoptError:
    print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
if len(opts) == 0:
    print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    elif opt in ("-f", "--filter"):
        filterstr = arg
print ('Input File: ', inputfile)
print ('Output file: ', outputfile)
print ('Filter String: ', filterstr)


outlist = ['a','a','a','a','a']

hourmin = "0000"
count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
    wr = csv.writer(outfile,dialect='excel')
    for l in infile:
        if l.find("HeartBeatService") != -1 and l.find(filterstr) != -1:
                     s = l.split(' ')
                     outlist[0]=s[0]
                     outlist[1]=s[1]
                     outlist[2]=s[2]
                     outlist[3]=s[3]
                     outlist[4]=s[14].rstrip()
                     wr.writerow(outlist)



