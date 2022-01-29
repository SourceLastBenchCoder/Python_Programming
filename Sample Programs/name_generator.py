import os
import random

os.system("cls")
print("Welcome to Name Generator")
keyword = input("Enter character to generate name?\n")

num_chr = 8

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
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "y"
]

name_generated = ""
name_list = []

for numData in range(1, 20):
    num = random.randint(5, 11)
    for char in range(1, num + 1):
        name_generated += random.choice(letter)
    name_list.append(keyword.upper() + name_generated)
    name_generated = ""

print(name_list)
