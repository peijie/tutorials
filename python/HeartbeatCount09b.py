
import os
import csv

os.chdir("E:\\UserData\\Projects\\Cubicon2\\Docs\\Log\\Offline\\SG-09B")


outlist = ['a','a','a','a','a']

hourmin = "0000"
count = 0

with open('S1-SVC-C2-09B-WLS_Plugin_D20160901-000000448.log', "r") as infile, open('HeartBeatCount09b.txt', "w") as outfile:
       ##wr = csv.writer(outfile,dialect='excel')
       for l in infile:
              if l.find("HeartBeatService") != -1:
                    s = l.split(' ')
                    tm = s[2][:5]
                    if tm != hourmin:
                        ##print out
                        ##print(tm + "," + str(count))
                        outfile.write(tm + "," + str(count) + "\n")
                        hourmin = tm
                        count = 0
                    else:
                        count += 1



##infile = open('S1-SVC-C2-09A-WLS_plugin_D20160830-000000032.log')
###outfile = open('out.csv', "w")
###wr = csv.writer(outfile, dialect='excel')
##
##
##
##for num in range(1,800):
##    l = infile.readline()
##    if l.find("HeartBeatService") != -1:
##        s = l.split(' ')
##        tm = s[2][:5]
##        if tm != hourmin:
##            ##print out
##            print(tm + "," + str(count))
##            hourmin = tm
##            count = 0
##        else:
##            count += 1

