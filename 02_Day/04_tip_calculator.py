# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print("Welcome to the tip calculator")
total_bill= int(input("Enter the amount of total bill"))
tip= int(input("enter the amount of tip you want to give"))
total_people= int(input("Enter the number of people the bill is to be shared"))
final_bill= total_bill*tip/100 + total_bill

print("The total amount after adding the tip is:", final_bill)
print("The amount each person have to pay:",final_bill/total_people)
