# Program Name: IT5413_A1_Prob1_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 1
# Problem Number: 1
# Last Update: 1/19/2021
# Purpose: Create program where you enter items & price and receive total price and list of items. 
# Note: I repeated myself a good bit, I am sure creating a for loop and using an array would work
 


##Intro
print("\r\n")
print("Welcome to Pa & Ma Grocery Store")
print("\r\n")
print("-------------------------------------")

##Item 1 
item1 = input("What do you want to purchase for Item #1? ")
item1_price = float(input("What is the price for " + item1 + "? "))
##Set two decimal points for price
item1_price_final = "{:.2f}".format(item1_price)
print("\r\n")

##Item 2 
item2 = input("What do you want to purchase for Item #2? ")
item2_price = float(input("What is the price for " + item2 + "? "))
##Set two decimal points for price
item2_price_final = "{:.2f}".format(item2_price)
print("\r\n")

##Item 3 
item3 = input("What do you want to purchase for Item #3? ")
item3_price = float(input("What is the price for " + item3 + "? "))
##Set two decimal points for price
item3_price_final = "{:.2f}".format(item3_price)
print("\r\n")

##Item 4 
item4 = input("What do you want to purchase for Item #4? ")
item4_price = float(input("What is the price for " + item4 + "? "))
##Set two decimal points for price
item4_price_final = "{:.2f}".format(item4_price)
print("\r\n")

##Item 5 
item5 = input("What do you want to purchase for Item #5? ")
item5_price = float(input("What is the price for " + item5 + "? "))
##Set two decimal points for price
item5_price_final = "{:.2f}".format(item5_price)
print("\r\n")

##Item 6
item6 = input("What do you want to purchase for Item #6? ")
item6_price = float(input("What is the price for " + item6 + "? "))
##Set two decimal points for price
item6_price_final = "{:.2f}".format(item6_price)
print("\r\n")

##Item 7 
item7 = input("What do you want to purchase for Item #7? ")
item7_price = float(input("What is the price for " + item7 + "? "))
##Set two decimal points for price
item7_price_final = "{:.2f}".format(item7_price)
print("\r\n")

##Item 8 
item8 = input("What do you want to purchase for Item #8? ")
item8_price = float(input("What is the price for " + item8 + "? "))
##Set two decimal points for price
item8_price_final = "{:.2f}".format(item8_price)
print("\r\n")

##Math to get receipt total 
total_price = item1_price + item2_price + item3_price + item4_price + item5_price + item6_price + item7_price + item8_price
total_price_final = "{:.2f}".format(total_price)

##Thank you message
print("Thank you for shopping at Pa & Ma Grocery Store!")
print("Here's your receipt!")
print("\r\n")


##Receipt
print(f"{'Item' : <15}{'Price' : ^10}") 
print(f"{'--------' : <15}{'---------' : ^10}") 
print(f"{item1 : <15}{'$' + str(item1_price_final) : ^10}")
print(f"{item2 : <15}{'$' + str(item2_price_final): ^10}")
print(f"{item3 : <15}{'$' + str(item3_price_final) : ^10}")
print(f"{item4 : <15}{'$' + str(item4_price_final) : ^10}")
print(f"{item5 : <15}{'$' + str(item5_price_final) : ^10}")
print(f"{item6 : <15}{'$' + str(item6_price_final) : ^10}")
print(f"{item7 : <15}{'$' + str(item7_price_final) : ^10}")
print(f"{item8 : <15}{'$' + str(item8_price_final) : ^10}")
print(f"{'-----' : <15}{'-----' : ^10}") 

##Total Price
print(f"{'Total' : <15}{'$' + str(total_price_final) : ^10}")
print(f"{'========' : <15}{'========' : ^10}") 