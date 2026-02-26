# Rent Calculator
# input we need from the user
# total food order 
# electricity unit spent
# carge per unit
# person living in the flat


# OUTPUT
# total bill amount

flat_rent = int(input("Enter Your Flate Rent = "))
food = int(input("Enter Your Total Food Order =  "))
electricity = int(input("Enter total of elelctricity spent = "))
charge_per_unit = int(input("Enter charge per unit = "))
person_living = int(input("Enter total number of person living in the flat = "))

totalbill = electricity * charge_per_unit

output = (food + flat_rent + totalbill) / person_living
print("Each person has to pay: ", output)