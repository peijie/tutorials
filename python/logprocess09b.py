
import os
import csv

os.chdir("E:\\UserData\\Projects\\Cubicon2\\Docs\\Log\\Offline\\SG-09B")


##infile = open('S1-SVC-C2-09A-WLS_plugin_D20160830-000000032.log')
##outfile = open('out.csv', "w")
##wr = csv.writer(outfile, dialect='excel')

outlist = ['a','a','a','a','a']

with open('S1-SVC-C2-09B-WLS_Plugin_D20160901-000000448.log', "r") as infile, open('logprocess09b.txt', "w") as outfile:
       wr = csv.writer(outfile,dialect='excel')
       for l in infile:
              if l.find("HeartBeatService") != -1:
                     s = l.split(' ')
                     outlist[0]=s[0]
                     outlist[1]=s[1]
                     outlist[2]=s[2]
                     outlist[3]=s[3]
                     outlist[4]=s[14].rstrip()
                     wr.writerow(outlist)
##
##
##
##for num in range(1,10):
##    l = infile.readline()
##    if l.find("HeartBeatService") != -1:
##        s = l.split(' ')
##        outlist[0]=s[0]
##        outlist[1]=s[1]
##        outlist[2]=s[2]
##        outlist[3]=s[3]
##        outlist[4]=s[14].rstrip()
####      last = s[14]
####      tm = last.split('\\');
####      outlist[4]=tm[0]
##        print(outlist)
##        wr.writerow(outlist)
##
##outfile.close()

