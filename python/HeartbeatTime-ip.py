
import sys
import getopt
import os

inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
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
print ('Input File: ', inputfile)
print ('Output file: ', outputfile)


#outlist = ['a','a','a','a','a']

hourmin = "0000"
count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
       for l in infile:
              if l.find("HeartBeatService") != -1:
                    s = l.split(' ')
                    tm = s[1][:5]
                    outfile.write(tm + "," + s[15] + "\n" )
                    

