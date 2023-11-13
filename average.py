counter = 0
numberslist = 0
while True: 
    number = int(input('Enter a number: '))
    numberslist += number
    if number <= 0:
        average = numberslist / counter
        print('the average of this numbers is :' , average)
        break  
    counter += 1   

 
    
