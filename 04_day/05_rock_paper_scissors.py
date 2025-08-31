import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors=[rock,paper,scissors]
choice_human=int(input("What's your choice, type '0' for rock, '1' for paper,'2' for scissors "))
choice_computer=random.choice([0,1,2])

if choice_human>=0 and choice_human<=2:
    print("your choice")
    print(rock_paper_scissors[choice_human])
    print("computer's choice")
    print(rock_paper_scissors[choice_computer])

    if choice_human==choice_computer:
        print("it is a draw")
    elif choice_human==0 and choice_computer==1:
        print("you lost")
    elif choice_human==0 and choice_computer==2:
        print("you won")
    elif choice_human==1 and choice_computer==0:
        print("you won")
    elif choice_human==1 and choice_computer==2:
        print("you lost")
    elif choice_human==2 and choice_computer==1:
        print("you won")
    elif choice_human==2 and choice_computer==0:
        print("you lost")
else:
    print("invalid number")


