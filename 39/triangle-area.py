from math import sqrt
l = []
while True:
    try:
        for i in range(0, 3):
            n = int(input('?'))
            if n != 0:
                l.append(n)
            else:
                raise Exception('please dont enter ziro')
        while True:
            if l[0]+l[1] <= l[2]:
                print('please insert a smaller number')
                l[2] = int(input('?'))    
            else:
                break 
        p = sum(l) / 2
        print(sqrt(p * (p-l[0])*(p-l[1])*(p-l[2])))  
        break
    except ValueError:
        print('please enter just number')
    except Exception as e:
         print(e)




