
# calories.py
# Author: Cody Vantienen
# Date: 11/09/2020
# Purpose - The purpace of this program is to create a loop to display the number of 
# calories burned after 10, 15, 20, 25, and 30 minuetes.
# Notes/Info: Running on a tredmill you burn 4.2 caolries per minute. 

#Create constant for calories burned per minute = 4.2
caloriesPerMin = 4.2

# declare variables for number of calories burned and the number of minutes.
mins = 0.0
caloriesBurned = 0.0


# Print table heading. 
print('Minutes\t\tCalories Burned')
print('- - - - - - - - - - - - - - - - - - - - - - - -' )

# Create loop to display time and calories burned.
for mins in range(10, 31, 5):
    caloriesBurned = mins * caloriesPerMin 
    print(mins, "\t\t", caloriesBurned)
