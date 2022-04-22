#!/usr/bin/env python3

#open file in read mode
with open("345-0.txt","r") as draculafile:
    #eachline = draculafile.readlines()
    linecount=0
    for eachline in draculafile:
        
        #eachline=eachline.rstrip('\n')
        if "vampire" in eachline.lower():
           # print(eachline)
            with open("vampireline.txt","a") as newfile:
                newfile.write(eachline+"\n")
            linecount+=1
    print (linecount)
