'''
Name: Trenton Alleman
Date: 9/27/2025
Assignment Name: P1HW2_AllemanTrenton
Discription: Creating a budget for the user
'''
 
'''
 Pseudocode for the program 
 #// input 
 Display "This program calculates and displays travel expenses"
 Display "Enter Budget"
 Input Budget
 Display "Enter your travel destination"
 Input Travel Destination
 Display "How much do you think you will spend on gas?"
 Input Fuel
 Display "Approximately, how much will you need for accomodation/hotel?"
 Input Accomodation 
 Display "lastly, How much do you need for food?
 Input Food

#// calculation
Remaining Balance = Buget - Fuel - Accomoodation - Food 

#// Output 
Display "Location:", Location
Display "Initial Budget:", Budget
Display "Fuel:", Fuel
Display "Accomodation:", Accomodation
Display "Food:", Food
Display "Remaining Balance:", Remaining Balance

'''

#// Input 
print("This program calculates and displays travel expenses")
Budget = int(input("Enter Budget"))
Travel_Destination = input("Enter your travel desination")
Fuel = int(input("How much do you think you will spend on gas?"))
Accomodation = int(input("Approximately, how much will you need for accomodation/hotel?"))
Food = int(input("Lastly, how much do you need for food?"))

#// calculation 
Remaining_Budget = Budget - Fuel - Accomodation - Food

#// Output 
print("Location:", Travel_Destination)
print("Initial Budget:", Budget)

print()
print("Fuel:", Fuel)
print("Accomodation:", Accomodation)
print("Food:", Food)

print()
print("Remaining Balance:", Remaining_Budget)
      
