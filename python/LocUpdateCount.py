
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
              if l.find("LocationService") != -1:
                    s = l.split('\t')
                    ##print(s[1][:5])
                    tm = s[1][:5]
                    if tm != hourmin and count > 0:
                        ##print out
                        ##print(tm + "," + str(count))
                        outfile.write(tm + "," + str(count) + "\n")
                        hourmin = tm
                        count = 0
                    else:
                        count += 1


