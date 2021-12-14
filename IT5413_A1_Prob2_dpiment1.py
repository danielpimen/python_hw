# Program Name: IT5413_A1_Prob2_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 1
# Problem Number: 2
# Last Update: 1/19/2021
# Purpose: Create simple program where you enter temperature in celsius and get temperature in fahrenheit 
# Note: 


##Formula for Celsius to Fahrenheit
## (x * 1.8) + 32 = Degrees Fahrenheit 

##Intro Text
print("")
print("Welcome to our Temperature Conversion App!")
print("===========================================")
print("")
celsius = float(input('Please enter today\'s Celsius temperature (e.g. 20): '))

##Global Variables 
degree_sign = u"\N{DEGREE SIGN}"
fahrenheit = float(((celsius * 1.8 ) + 32))

##Convert to String
celsius_string = str(celsius)
fahrenheit_string = str(fahrenheit)


####Output 
print("")
print("Today\'s temperature from Celsius to Fahrenheit")
print('===============================================')
print("Temperature " + celsius_string + degree_sign +'C' ' ==> ' + fahrenheit_string + degree_sign + 'F')
print("")
print('Thank you for using our Temperature Conversion App')