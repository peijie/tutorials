
import sys
import getopt
import os
import time
import datetime
import calendar
from datetime import datetime

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
tm0 = time.gmtime(0)
dt0 = datetime.strptime('01/01/2001 1:00:00 AM', '%d/%m/%Y %I:%M:%S %p')

count = 0

with open(inputfile, "r") as infile, open(outputfile, "a") as outfile:
       for l in infile:
              if l.find("Location Update") != -1 or l.find("Incident Record") != -1:
                    s = l.split(' ')
                    ##print (l)
                    tm = s[1][:5]

                    #tmstr = l[:20].strip()
                    pm = s[2].split('\t')
                    tmstr = (s[0] + " " + s[1] + " " + pm[0]).strip()

                    
##                    if (len(tmstr) < 20):
##                        ## add 0 before hour
##                        tmstr = l[:9] + "0" + l[9:20]
##                        print (tmstr)

                    ##tm1 = time.strptime(tmstr, '%d/%m/%Y %I:%M:%S %p')
                    try:
                        dt1 = datetime.strptime(tmstr, '%m/%d/%Y %I:%M:%S %p')
                    except:
                        print (tmstr)
                    

                    


                    ##print (l[:20])
##                    try:
##                        tm1 = time.strptime(tmstr, '%d/%m/%Y %I:%M:%S %p')
##                    except:
##                        print (l[:20])
                                       
                    ##print (l[:20] + "----->" + time.strftime('%d/%m/%Y %I:%M:%S %p', tm1) )

                    if (dt1-dt0).total_seconds() > 120:
                    ##if (calendar.timegm(tm1) - calendar.timegm(tm0)) > 120:
                    ##if tm != hourmin and count > 0:
                        ##print out
                        ##print(tm + "," + str(count))
                        if (hourmin != "0000"):
                            outfile.write(hourmin + "," + str(count) + "\n")
                        hourmin = tm
                        ##tm0 = tm1
                        dt0 = dt1
                        count = 0
                    else:   
                        count += 1


