from random import choice , randint
firstnames = []
names=[]
with open('firstname.txt' , encoding="utf-8") as f:
    for line in f.readlines():
        firstnames.append(line.split()[1].strip())

lastnames = []
with open('lastname.txt' , encoding="utf-8") as f:
    for line in f.readlines():
        lastnames.append(line.split()[1].strip())

for i in range(40):
    firstname = choice(firstnames)
    lastname = choice(lastnames)
    score = randint( 60 , 80) / 4
    s = f'{firstname} {lastname} ,{score}'
    names.append(s)
print(names)
with open('data.txt' , 'w', encoding="utf-8") as f:
    f.write('\n'.join(names)) 
# print(data)

