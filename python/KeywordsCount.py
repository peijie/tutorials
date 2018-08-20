
import sys
import getopt
import time
import datetime
import calendar
from datetime import datetime

inputfile = ''
outputfile = ''
interval = 120
keywords = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:t:", ["ifile=", "ofile=", "tinterval="])
except getopt.GetoptError:
    print ('Usage: KeywordsCount.py -i <inputfile> -o <outputfile> -t <interval>  keyword1 keyword2')
    sys.exit(2)
if len(opts) == 0:
    print ('Usage: KeywordsCount.py -i <inputfile> -o <outputfile> -t <interval>  keyword1 keyword2')
    sys.exit(2)
    
if len(args) == 0:
    print ('Usage: KeywordsCount.py -i <inputfile> -o <outputfile> -t <interval>  keyword1 keyword2')
    sys.exit(2)

keywords = args

for opt, arg in opts:
    if opt == '-h':
        print ('Usage: KeywordsCount.py -i <inputfile> -o <outputfile> -t <interval>  keyword1 keyword2')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
    elif opt in ("-t", "--tinterval"):
        interval = int(arg)
print ('Input File: ', inputfile)
print ('Output file: ', outputfile)
print ('Keywords: ', keywords)
print ('Interval: ', interval)


hourmin = "0000"
tm0 = time.gmtime(0)
dt0 = datetime.strptime('01/01/2001 1:00:00 AM', '%d/%m/%Y %I:%M:%S %p')

count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
    for l in infile:
        if any(x in l for x in keywords):
            s = l.split(' ')
            tm = s[1][:5]

            pm = s[2].split('\t')
            tmstr = (s[0] + " " + s[1] + " " + pm[0]).strip()

            try:
                dt1 = datetime.strptime(tmstr, '%m/%d/%Y %I:%M:%S %p')
            except:
                print (tmstr)
                    
            if (dt1-dt0).total_seconds() > interval:
                if (hourmin != "0000"):
                    outfile.write(hourmin + "," + str(count) + "\n")
                hourmin = tm
                dt0 = dt1
                count = 0
            else:   
                count += 1


