print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        amount=500
        print("The price of child ticket is 500")
    elif age <= 18:
        amount=1000
        print("The price of teenager ticket is 1000")
    else:
        amount=1500
        print("The price of adult ticket is 1500")

    wants_pic=input("Do you want to click photos? Type 'y' for yes and 'n' for no ")
    if wants_pic== "y":
         amount+=300
    print(f"your final bill is {amount}")

else:
    print("Sorry you have to grow taller before you can ride.")
