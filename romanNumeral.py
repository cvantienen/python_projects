# Chapter 3 Problem 2
# ageClassifier.py
# Author: Cody Vantienen
# Date: 10/7/20
# Purpose: Write a program in which a user can enter a number 1-10, and gives corrisponding roman numeral
#          numbers entered that are not 1-10, error message should display.
# Notes: 
# 1 = I         6 = VI
# 2 = II        7 = VII
# 3 = III       8 = VIII
# 4 = IV        9 = IX
# 5 = V         10 = X

# input section 
integer = int(input("Enter an integer from 1 - 10: "))
print()

# working variable
romanNumeral = "N/A"

# Algorithm/Conditional Processing
if integer == 1:
 romanNumeral ="I"
elif integer == 2:
    romanNumeral ="II"
elif integer == 3:
    romanNumeral ="III"
elif integer == 4:  
    romanNumeral ="IV"
elif integer == 5:
    romanNumeral ="V"
elif integer == 6:
    romanNumeral ="VI"
elif integer == 7:
    romanNumeral ="VII"
elif integer == 8:
    romanNumeral ="VIII"
elif integer == 9: 
    romanNumeral ="IX"
elif integer == 10:
    romanNumeral ="X"
else:
 romanNumeral = "Invalid value entered"

# output section
print("The roman numeral is: ", romanNumeral)
               
       
  
  
    