from random import randint
number = randint(1,40)
for i in range(1,6):
    a = int(input('Enter your number: '))
    if a == number:
        print('wellDone!!')
        break
    elif a > number and a != 0:
        print(' insert smaller')
    elif a > 40 or a < 1:
        print('please insert a number between 1 and 40')
    else:
        print(' insert greater')
else:
    print(' we are sorry you lost!')