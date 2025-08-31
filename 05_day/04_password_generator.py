import random
from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# random_letters=random.choices(letters,k=nr_letters)
#
#
# random_numbers=random.choices(numbers,k=nr_numbers)
#
#
# random_symbols=random.choices(symbols,k=nr_symbols)
#
#
# let_num_sym=random_letters+random_symbols+random_numbers
#
#
# random.shuffle(let_num_sym)
# password=''.join(let_num_sym)
# print(password)


# OR
password=""

# for character in range(1,nr_letters+1):
#     char=random.choice(letters)
#     # print(char)
#     password+=char
# for num in range(1,nr_numbers+1):
#     a=random.choice(numbers)
#     # print(a)
#     password+=a
# for special_characters in range(1,nr_symbols+1):
#     sym=random.choice(symbols)
#     # print(sym)
#     password+=sym
# print(password)
# random.shuffle(password)
# print(password)

#hard

password_list=[]

for character in range(1,nr_letters+1):
    char=random.choice(letters)
    # print(char)
    password_list+=char
for num in range(1,nr_numbers+1):
    a=random.choice(numbers)
    # print(a)
    password_list+=a
for special_characters in range(1,nr_symbols+1):
    sym=random.choice(symbols)
    # print(sym)
    password_list+=sym

random.shuffle(password_list)
print(password_list)

# password=""
# for character in password_list:
#     password+=character
# print(password)

# you can do it in a short form

password=''.join(password_list)
print(password)

