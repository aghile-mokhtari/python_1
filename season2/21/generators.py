# # ///first number///
# prime_number = [2]
# def prime_numbers(n):
#     for i in range(3,n,2):
#         for p in prime_number:
#             if i % p == 0:
#                 break
#         else:
#             yield i
# for i in prime_numbers(100):
#     prime_number.append(i)
# print(prime_number)



# ////fibonacci///
# list =[1,1]
# def fibo(n):
#     if n < 3:
#         return 1
#     else:
#         for i in range (0,n-2):
#             x = (list[i])+(list[i+1])
#             yield x
           
# for i in fibo(8):
#     list.append(i)
# print(list[(len(list)-1)])



# ///tibonacci///// 
# list =[0,0,1]
# def fibo(n):
#     if n < 3:
#         return 0
#     elif n == 3:
#         return 1
#     else:
#         for i in range (0,n-3):
#             x = (list[i])+(list[i+1])+(list[i+2])
#             yield x
           
# for i in fibo(1):
#     list.append(i)
# print(list[(len(list)-1)])
# 


# ////power of n//// 
# list = [1]
# def power(n):
#     for i in range(0,10):
#         x = n*list[i]
#         yield x
# for i in power(2):
#     list.append(i)
# print(list)



# /////factorial//// 
# list = [1]
# def fac(n):
#     x = 1
#     if n == 1:
#         return 1
#     else:
#         for i in range(1,n):
#             x = x * (i+1)
#         yield x
            
# for i in fac(5):
#     print(i)



# //////اعداد تام/////////
# tamam=[]
# def per(n):
#     for i in range(1,n):
#         list=[]
#         for x in range(1,i):
#             if (i % x == 0):
#                 list.append(x)
#         if(sum(list) == i):
#             yield i   

# for i in per(100):
#    tamam.append(i) 
# print(tamam)
