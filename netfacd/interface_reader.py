#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
#        print(netifaces.ifaddresses(i))
#        print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        try:

            print("MAC Address: ",netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print("IP Address: ",netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information')

