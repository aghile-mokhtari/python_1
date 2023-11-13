from random import randint
number = randint(1,40)
s = 0
while True:
    a = int(input('Enter your number: '))
    if s == 5:
        print(' we are sorry you lost!')
        break
    elif a == number:
        print('wellDone!!')
        break
    elif a > number and a != 0:
        print(' insert smaller')
    elif a > 40 or a < 1:
        print('please insert a number between 1 and 40')
    else:
        print(' insert greater')
    s += 1
print(number)

