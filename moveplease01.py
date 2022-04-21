#! /usr/bin/env python3

#importing standard libraries
import shutil
import os

def main():
    #move to working directory; called at runtime
    os.chdir("/home/student/mycode/")
    
    #moving file from working directory to another directory; in this case ceph_storage directory
    shutil.move('raynor.obj','ceph_storage/')
    
    #asking for user input to what to rename the file to
    xname=input('What is the new name for kerrigan.obj?')

    #calling shutil library, and using move method to rename file
    shutil.move('ceph_storage/kerrigan.obj','ceph_storage/' + xname)

if __name__ == "__main__":
    main() #to call main function


