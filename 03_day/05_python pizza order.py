print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size== "S":
    amount = 15
    print("That will cost you $15")
elif size =="M":
    amount= 20
    print("That will cost you $20")
elif size=="L":
    amount= 25
    print("That will cost you $25")
else:
    print("invalid input")
    exit()


pepperoni = input("Do you want pepperoni on your pizza? Y for 'yes' or N 'No': ")
if pepperoni=="Y":
    if size=="S":
        amount+=2
        print("That will cost you $2")
        print(f"The total amount is ${amount}")
    else:
        amount+=3
        print("That will cost you $3")
        print(f"The total amount is ${amount}")


extra_cheese = input("Do you want extra cheese? Y or N:")
if extra_cheese=="Y":
    amount+=1
    print("That will cost you $1")
    print(f"The bill is ${amount}")
else:
    print(f"The total amount to be paid is ${amount}")
