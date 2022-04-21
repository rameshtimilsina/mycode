#!/usr/bin/env python3

import uuid

num = int(input("How many UUIDs do you want to create? "))

print ("Generating UUIDs...")

for x in range(num):
    print(uuid.uuid4())

