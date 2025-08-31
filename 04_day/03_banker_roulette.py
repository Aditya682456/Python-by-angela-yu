import random
from random import randint

#1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_element=random.choice(friends)
print(f"{random_element} have to pay the bill")

#2
random_index=randint(0,4)
print(friends[random_index])