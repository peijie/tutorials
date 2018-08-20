
import sys
import getopt
import os

inputfile = ''
outputfile = ''
keyword = ''


try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:k:", ["ifile=", "ofile="])
except getopt.GetoptError:
    print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile> -k keyword')
    sys.exit(2)
if len(opts) == 0:
    print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile>  -k keyword')
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        print ('Usage: HeartbeatCount.py -i <inputfile> -o <outputfile>  -k keyword')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    elif opt in ("-k", "--keyord"):
        keyword = arg
print ('Input File: ', inputfile)
print ('Output file: ', outputfile)


#outlist = ['a','a','a','a','a']

hourmin = "0000"
count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
       for l in infile:
              if l.find(keyword) != -1:
                    s = l.split(' ')
                    tm = s[2][:5]
                    outfile.write(tm + "," + s[14])
                    

