# Chapter 3 Problem 4
# order.py
# Author: Cody Vantienen
# Date: 10/7/20
# Purpose: Write a program that can determine if 3 float values entered by user are increasing order, decresing order, or neither. 
# Notes: 

# input section 
numOne = float(input("Enter the fisrt number: "))
numTwo = float(input("Enter the Second number: "))
numThree = float(input("Enter the third number: "))

# algorithm / conditional processing
if numOne < numTwo and numTwo < numThree:
    print("They are in increasing order")
elif numOne > numTwo and numTwo > numThree:
    print("They are in decreasing order")
else: 
    print("They are not increasing or decreasing")
    
        
        
            
 
  
