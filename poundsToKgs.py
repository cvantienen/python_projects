# Chapter 2 Lab Problem 1 # poundsToKgs.py
# Author: Cody Vantienen
# Date: 9/30/20
# Purpose: Write a program that converts weight entered 
#          by user in pounds to kilograms
# Notes: 1 pound is equal to .45 kilograms 
#        ex. 43 pounds = 43 * .45 = 19.35 kilograms

LBS_TO_KGS = .45

# input Section 
weightInPounds = int(input("Enter a value in pounds: "))
print()
# process Section 
weightInKilograms = weightInPounds * LBS_TO_KGS 

# output Section 
print(weightInPounds, " pounds is ", format(weightInKilograms, '.2f'), " kilograms.") 

#end


