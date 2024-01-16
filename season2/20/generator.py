from random import randint

def read_text(filename):
    with open(filename , encoding="utf-8") as f:
        for line in f:
            yield line.split()[1].strip()

for name , famil in zip(read_text('firstname.txt') ,read_text('lastname.txt') ):
    print(name , famil)

# def x(n):
#     for i in range(n):
#         yield randint(1,100)

# for i in x(20):
#     print(i)
