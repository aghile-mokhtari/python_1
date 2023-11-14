
couple_number = []
n = 1000
prime_number =[2]
for i in range(3,n,2):
    for j in prime_number:
        if i % j == 0:
            break
    else:
        prime_number.append(i)
        index_i = prime_number.index(i)
        first_number = prime_number[index-1]
        if i - 2 == first_number:
           couple_number.append([first_number, i])
print(couple_number)