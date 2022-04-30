names = ['appu','chakrapani','upadhyaya',23,'TRUE']

for name in names:
    print(name)

print(names[0])

print(names[2:4])

names.insert(2,"Shraddha")
print(names)

names.append("Shreshta")
print(names)

names.append("Shreshta")
print(names)

names[2]="Updated"
print(names)

names.remove("Updated")
print(names)

rec = names.pop(2)
print(rec)
print(names)