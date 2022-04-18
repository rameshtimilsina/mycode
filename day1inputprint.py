#!/usr/bin/env python3

import random
#Include the following list
icecream = ["indentation","spaces"]

#Include this list of students
tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]
reversestudents=list(reversed(tlgstudents)) #reversing the list
#Appending integer 4 to the icecream list
icecream.append(int(4))

#Ask for a number between 0 and 17
selection = input("Please enter a numberbetween 0 to 17: ")

#use the number entered to print the student from tlgstudents list
print(f"Original list is: \n {tlgstudents}") #print the list tlgstudents
print(f"List reversed is: {reversestudents}")
print(f"Student from the list that corresponds to number {int(selection)} is: {tlgstudents[int(selection)]}") #prints the value of entered number's from tlgstudents list

#print random student

print(f"Randomly selected student is: {random.choice(tlgstudents)}")




