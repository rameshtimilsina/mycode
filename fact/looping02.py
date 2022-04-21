#!/usr/bin/env python3

#open file in read mode

dnsfile=open("dnsservers.txt","r")

#create list of lines
dnslist=dnsfile.readlines()

for svr in dnslist:
    #print and end without a newline
    print(svr,end="") # this line we read already contains a\n (newline)

#close the file
dnsfile.close()

