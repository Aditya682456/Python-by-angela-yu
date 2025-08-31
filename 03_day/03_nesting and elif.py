print("welcome to our amusement park!!")
height = int(input('Enter your heignt(in cm):'))
if height>120:
    print("You can enter the park")
    age=int(input("Enter your age"))
    if age<=12:
        print("you have to pay Rs 500")
    elif age<18:
        print("you have to pay Rs 1000")
    else:
        print("you have to pay Rs 1500")
else:
    print("you cant enter the park")