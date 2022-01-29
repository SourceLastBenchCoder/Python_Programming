import random
from os import system

system("cls")

letter = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

sybmol = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "+"]

password = ""
password_list = []

print("Welcome to Password Generator")
nr_letters = int(input("How Many letter do you need ?\n"))
nr_numbers = int(input("How Many number do you need ?\n"))
nr_symbols = int(input("How Many symbols do you need ?\n"))

for char in range(1, nr_letters + 1):
    password_list += random.choice(letter)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(number)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(sybmol)

random.shuffle(password_list)

for char in password_list:
    password += char

print(f"Generated Password is below\n{password}")
