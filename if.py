day = int(input('Enter a number between 1 and 30 :'))
if day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
    print('Monday') 
elif day == 2 or day == 9 or day == 16 or day == 23 or day == 30:
    print('Tuesday') 
elif day == 3 or day == 10 or day == 17 or day == 24:
    print('Wednesday') 
elif day == 4 or day == 11 or day == 18 or day == 25:
    print('Thursday') 
elif day == 5 or day == 12 or day == 19 or day == 26:
    print('Friday') 
elif day == 6 or day == 13 or day == 20 or day == 27:
    print('Saturday') 
elif day == 7 or day == 14 or day == 21 or day == 28:
    print('Sunday') 
else:
    print('your number is invalid')

