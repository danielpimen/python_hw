# Program Name: IT5413_A3_Prob1_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 3
# Problem Number: 1
# Last Update: 2/14/2021
# Purpose: Create an app where you enter your name & 8 test scores and get letter grade for each test, final average, and final letter grade as output
# Note: I feel like i could have made this simplier. I feel like I made too many variables


##Intro Text 
print('')
print('Welcome to Test Score Calculator')
print('---------------------------------')

##Function accepts 8 test scores and returns average 
def calc_average(grade_list) : 
    return sum(grade_list)/ len(grade_list)


##Function accepts test score average returns letter grade individual test letters 
def determine_grade(grade_list, student_average) : 

    ##List for append letter grades for each test letter
    letter_grades = []

    ##for loop to calculate letter grade
    for i in grade_list: 
        if i >= 90:
            letter_grades.append('A')
        elif i >= 80: 
             letter_grades.append('B')
        elif i >= 70 : 
            letter_grades.append('C')
        elif i >= 60 : 
            letter_grades.append('D')
        else : 
            letter_grades.append('F')

    ##if-else statement to determine final grade letter 
    if student_average >= 90 : 
        final_letter_grade = 'A'
    elif student_average >= 80: 
        final_letter_grade = 'B'
    elif student_average >= 70 : 
        final_letter_grade = 'C'
    elif student_average >= 60 : 
        final_letter_grade = 'D'
    else : 
        final_letter_grade = 'F'

    ##Export letter grades & final grade
    return letter_grades, final_letter_grade


##Function to get student name & grades & final output
def student_info() : 

    #Tracks number of tests 
    count = 1
    grade_list = []

    ##Get student name 
    student_name = input('Enter your name: ')

    ##while loop to get input 
    while count <= 8 : 

        ##Used F string to input test number in input statement
        test_score = int(input(F'Enter your 8 test scores - Test{count} score: '))

        if test_score >= 101 or 0 > test_score: 
            print('Please enter a number between 0 and 100')
        else: 
            count = count + 1
            ##List for grades, when user enters grade for a test, it is pushed to a list
            grade_list.append(test_score)

    ##Call calc_average function to calculate average, exports student avg
    student_average = calc_average(grade_list)

    ##Calculate Letter grade for each test, exports list with grade letters
    letter_grades, final_letter_grade = determine_grade(grade_list, student_average)

    ##Turn grade_list & letter_grades into a tuple for easier print
    final_output = list(zip(grade_list, letter_grades))

    ##Update format of student average to two decimal points 
    student_average = "{:,.2f}".format(student_average)

    ##Print out Final Results
    print('')
    print('Student Name:', student_name)
    print('')

    ##Create a count variable to act as counter for output
    count = 1

    ##Loop through tuple to print out scores & letter grade
    for x, y in final_output: 
        print('Test', count, 'Score:', x, '==> Grade:', y)
        count = count + 1

    ##Print Remaining text with student average and final letter grade
    print('')
    print('The average of the 8 test scores is:', student_average)
    print('Your overall grade for all the tests is:', final_letter_grade)

##Call student_info() function to start program
##Closing student_info() to print exception if any error during program
try:
    student_info()
except Exception as ex:
    print('Whoops, looks like something went wrong! Please make sure you only enter your name as well as number grades.')
    print(ex)

