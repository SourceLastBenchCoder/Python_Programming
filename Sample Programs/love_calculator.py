import os

os.system('cls')

print("Welcome to Love Calculator")

your_name = input("Enter your name : ")
partner_name = input("Enter your partner name : ")

name_both = your_name + partner_name

t = name_both.count("t")
r = name_both.count("r")
u = name_both.count("u")
e = name_both.count("e")

true = t + r + u + e

l = name_both.count("l")
o = name_both.count("o")
v = name_both.count("v")
e = name_both.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if score > 50:
    print("Your have excelent true love")
elif score > 40 and score < 50:
    print("Your have very good true love")
elif score > 30 and score < 40:
    print("Your have good true love")
elif score > 20 and score < 30:
    print("Your have avarage true love")
else:
    print("you do not have true love")
