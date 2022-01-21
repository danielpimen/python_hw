# Program Name: IT5413_A3_Prob2_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 3
# Problem Number: 2
# Last Update: 2/14/20
# Purpose: Create program that takes user input of Fahrenheit or Celsius, converts it and provides recommendations on what to wear 
# Note : 

##Degree sign 
degree_sign = u"\N{DEGREE SIGN}"

##Function to restart user_input
def restart(): 
    user_input()

##Function for user input 
def user_input(): 
    ##Intro Text 
    print('')
    print('Welcome to our Temperature Conversion and Weather Advisory App')
    print('---------------------------------------------------------------')
    print('')
    print('1) Celsius to Fahrenheit with Weather Advisory')
    print('2) Fahrenheit to Celsius with Weather Advisory')
    print('3) Quit')
    print('')

    ##Grab User Input 
    user_choice = int(input('Enter your choice (1, 2, or 3): '))

    ##if-else to direct to correct function(c2f,f2c, or break)
    if user_choice == 1 : 

        ##Get users input 
        current_temp = int(input('Enter your current temperature in Celsius: '))
       
        ##Call function to convert celsius to fahrenheit 
        f_temp = c2f(current_temp)
       
        ##Print current temp string 
        print("The current temperature:" , current_temp , degree_sign ,'C' ' ==>', f_temp, degree_sign, 'F')
        
        ##Call advice function to return string of advice
        temp_advice = advice(f_temp)
        
        print(temp_advice)
        ##Call function to restart 
        restart()

    elif user_choice == 2 : 
        
        ##Get Users input 
        current_temp = int(input('Enter your current temperature in Fahrenheit: '))
        
        ##Call f2c function to convert fahrenheit to celsius 
        c_temp = f2c(current_temp)
        
        ##Print both temps 
        print("The current temperature:" , current_temp , degree_sign ,'F' ' ==>', c_temp, degree_sign, 'C')
        
        ##Call advice function to return string of advice
        temp_advice = advice(current_temp)
        print(temp_advice)

        ##Call function to restart 
        restart()

    elif user_choice == 3: 

        ## if 3 is selected, program will end 
        print('Thank you for using our Temperature Conversion & Weather Advisory App')
        print('Please Come Again')
        exit

    else: 

        ##Function restarts if 1 2 or 3 is not selected 
        print('Oops, please click 1, 2 , or 3')
        user_input()
        
##Function to convert temperature for Celsius to Fahrenheit 
def c2f(current_temp): 
    fahrenheit_temp =  (current_temp * 1.8) + 32
    return fahrenheit_temp

##Function to convert temperature for Fahrenheit to Celsius
def f2c(current_temp): 
    celsius_temp =  (current_temp - 32) * .56
    return celsius_temp


##Function to give user advice on what to wear 
def advice(x): 
    if x < 0 : 
        temp_advice = 'It is extremely cold now; you want to really bundle up. Put on your heavy coat, flurry hat, wool scarf, and leather gloves.'
    elif x <= 32 : 
        temp_advice = 'It is very cold now; you want to wear your leather jacket, hat, scarf & gloves.'
    elif 32 <= x < 50: 
        temp_advice = 'It is cold now; you want to wear your good jacket with a scarf'
    elif 50 <= x < 68 : 
        temp_advice = 'It is cool now; you want to wear a jacket.'
    elif 68 <= x < 78 : 
        temp_advice = 'It is mild now; you want to wear a long sleeve shirt.'
    elif 78 <= x < 88 : 
        temp_advice = 'It is pleasant now; you can wear anything you want.'
    elif 88 <= x < 95 : 
        temp_advice = 'It is hot now; you can wear shorts today.'
    elif x > 95 : 
        temp_advice = 'It is very hot now; you may want to go swimming.'
    
    ##Export string of advice
    return temp_advice

##Call the user input function to get application started
user_input()



