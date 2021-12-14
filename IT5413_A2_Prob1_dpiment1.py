# Program Name: IT5413_A2_Prob1_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 2
# Problem Number: 1
# Last Update: 1/28
# Purpose: Create a program that will calculate tuition for the next 7 years for part-time & full-time students
# Note: I used f string to align output. I also use format function to add comma & two decimal points to currency 

###Introduction Text 
student_status = input("Please enter p if you are a part-time student, enter f if you are a full-time student: ")

###Starting Variables 
full_tuition = 6549
part_tuition = 3325
rate_increase = 1.035
start_year = 2021

###If-else statement to determine which code block to run for calculations
if student_status == 'f':
    print('')
    print('Here is the tuition information for a full-time student: ')
    print('---------------------------------------------------------')
    print('')
    print(f"{' Year' : <10}{'Tuition' : ^12}") 
    print(f"{'------' : <11}{'---------' : ^10}") 

##For loop to print the prices for full tuition 
    for x in range(8):

##I created f_tuition to format the tuition price so that it appears with $ and a comma 
        f_tuition = "${:,.2f}".format(full_tuition)
        print(f" {start_year : <10}{(f_tuition) : ^10}")

##multiply tuition so that the full_tuition variable updates 
        full_tuition = full_tuition *rate_increase  

##Updates the year by adding one to variable 
        start_year = start_year + 1   


elif student_status == 'p':
    print('')
    print('Here is the tuition information for a part-time student: ')
    print('---------------------------------------------------------')
    print('')
    print(f"{' Year' : <10}{'Tuition' : ^12}") 
    print(f"{'------' : <11}{'---------' : ^10}") 

##for loop to print the prices for part time tuition 
    for x in range(8):

##I created p_tuition to format the tuition price so that it appears with $ and a comma 
        p_tuition = "${:,.2f}".format(part_tuition)
        print(f" {start_year : <10}{(p_tuition) : ^10}")

##multiply tuition so that the full_tuition variable updates 
        part_tuition = part_tuition *rate_increase 

##Updates the year by adding one to variable  
        start_year = start_year + 1   
    
##this will appear if the user does not enter f or p 
else:
    print('Please enter f or p')
