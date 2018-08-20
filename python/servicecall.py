
import sys
import getopt
import os
import csv

inputfile = ''
outputfile = ''
filterstr = ''
servicename = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:s:f:", ["ifile=", "ofile=", "service=", "filter="])
    print('argv = ', sys.argv)
    print('opts = ', opts)
except getopt.GetoptError:
    print ('Usage: servicecall.py -i <inputfile> -o <outputfile> -s <servicename> -f <filter>')
    sys.exit(2)
if len(opts) == 0:
    print ('Usage: servicecall.py -i <inputfile> -o <outputfile> -s <servicename> -f <filter>')
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        print ('Usage: servicecall.py -i <inputfile> -o <outputfile> -s <servicename> -f <filter>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    elif opt in ("-s", "--service"):
        servicename = arg
    elif opt in ("-f", "--filter"):
        filterstr = arg

if inputfile == '' or outputfile == '' or servicename == '':
    print ('Usage: servicecall.py -i <inputfile> -o <outputfile> -s <servicename> -f <filter>')
print ('Input File: ', inputfile)
print ('Output file: ', outputfile)
print ('Service Name: ', servicename)
print ('Filter String: ', filterstr)


outlist = ['a','a','a','a','a']

hourmin = "0000"
count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
    wr = csv.writer(outfile,dialect='excel')
    for l in infile:
        if servicename != '' and filterstr != '' and l.find(servicename) != -1 and l.find(filterstr) != -1:
                     s = l.split(' ')
                     outlist[0]=s[0]
                     outlist[1]=s[1]
                     outlist[2]=s[2]
                     outlist[3]=s[3]
                     outlist[4]=s[14].rstrip()
                     wr.writerow(outlist)
        if servicename != '' and filterstr == '' and l.find(servicename) != -1:
                     s = l.split(' ')
                     outlist[0]=s[0]
                     outlist[1]=s[1]
                     outlist[2]=s[2]
                     outlist[3]=s[3]
                     outlist[4]=s[14].rstrip()
                     wr.writerow(outlist)



