#!/usr/bin/env python3

#assign data to farms variable

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#PRINT ALL THE LIST OUT
for x in farms:
    print (x)

#PRINT OUT ALL THE ANIMALS ON THE NE FARM

for x in farms:
    if (x.get("name") =="NE Farm"):
       # print (x)
        print(f"The animals in NE Farm are: {x['agriculture']}")


#PRINT OUT ONLY THE NAMES OF FARMS

for x in farms:
    print(x.get("name"))

getfarmname=input("Enter a farm name: (Options are NE Farm, W Farm, SE Farm)").lower()

for x in farms:
#print(f"The agriculture of {getfarmname} are: ")
    if (x.get("name").lower()==getfarmname):
        print (f"The agriculture in {getfarmname} are: {x['agriculture']}")





