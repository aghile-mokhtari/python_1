
number = int(input('Enter your number : '))
counter = 1
result = 0
while counter < number / 3:
    result = number / counter
    if result == counter:
        print('true')
        print('the root is',result)
        break
    elif counter == number / 3:
        print('false')
        break
    else:
        counter += 1
    
