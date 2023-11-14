counter = 0
numberslist = 0
while True: 
    number = int(input('Enter a number: '))
    if number <= 0:
        if counter != 0:
            average = numberslist / counter
            print('the average of this numbers is :' , average) 
            break   
        else:
            print('please insert a number greater than ziro')     
 
    numberslist += number
    counter += 1   
  
        

