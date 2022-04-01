# Lab 4 problem 2
# distanceTraveled.py
# Author: Cody Vantienen
# Date: 11/09/2020
# Purpose:  Create a program gets the user to enter the speed of a vehicle, and the number of hours
# traveled. Use a loop to calculate and display the distance traveled in hour intervals. 
# Notes: distance = speed * time

# Declare avariables for caluclating distance traveled 
distance = 0
speed = 0.0
time = 0

# Input section 
# Have user enter the speed of the vehicle and number of hours traveled 
speed = float(input("Enter the speed of the vehicle in mph:"))
time = int(input("Enter the number of hours traveled:"))

# Input validation to make sure they not entering crazy values
while speed < 0 or time < 0:
    print("Please enter values greater than 0")
    speed = int(float(input("Enter the speed of the vehicle in mph:")))
    time = int(input("Enter the number of hours traveled:"))
 
# Display the header for hours and distance traveled
print("Hour\tDistance Traveled")
print("- - - - - - - - - - - - - - - - - - - -")
 
 # Create loop to calculate and display the amount of hours and corrisponding distance traveled. 
 # hour is the traget variable 
for hour in range(1, time + 1): 
    distance = hour * speed 
    print(hour, "\t\t", distance) 
    
# End
 
    
    


