# from unicodedata import digit



# def getSum(n):

#     sum = 0
#     for digit in str(n):
#         sum +=int(digit)
#     return sum    
     
# n= int(input("enter digit:"))
# print(getSum(n)) 


# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.pop(0)
# print(stack)

# import collections
# from xmlrpc.client import Boolean


# queue = collections.deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.appendleft(12)
# queue.pop()
# not queue
# print(queue)

# x = 0

# while(x<100):
#     print(x)
#     x+=2

# sum = 0
# for i in range(1,1000):
#     if (i%3==0)or (i%5==0):
#         sum += i
# print(sum) 
# count = 0
# # nth = 0
# Esum= 0
# n1 =0
# n2= 1
# while(count<=4000000):
#      print(n1)  
#         nth = n1 + n2  
#        # At last, we will update values  
#         n1 = n2  
#         n2 = nth  
#         count += 1
# for i in n1:
#     if i%2==0:
#                 Esum +=i
#     print(Esum)             


# n = 100
# n1 = 0
# n2= 1
# count = 0
# sum= 0
# while(count<n):
#     print(n1)
#     nth  =n1+n2
#     n1 = n2
#     n2 = nth
#     count +=1
# for i in n1:
#     if i%2==0:
#         sum +=i
# print(sum)            

# limit=4000000
# sum=0
# a=1
# b=1
# while b<limit:
#     if b %2==0:
#         sum=sum+b
#     h=a+b
#     a=b
#     b=h
# print(sum)

# n=600851475143 
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)        

# num=600851475143
# i=2 # Smallest prime factor
# for k in range(0,num):
#     if i >= num: # Prime factor of the number should not be greater than the number
#         break
#     elif num % i == 0: # Check if the number is evenly divisible by i
#         num = num / i
#     else:
#         i= i + 1
# print ("biggest prime number is: "+str(num))   




#####DOUT####
# def gcd(x,y): return y and gcd(y, x % y) or x
# def lcm(x,y): return x * y / gcd(x,y)

# n = 1
# for i in range(1, 21):
#      n = lcm(n, i)
# print(n)






# from ast import Num
# import math
# def fact(n):
#    return 1 if (n ==0 or n==1)  else n*fact(n-1);
   
# num = int(input("enter num :"))
# print(f"factorial of {num} is")
# f =fact(num)
# print(f)
# n = 10
# factorial  =1
# for i in range(1,n+1):
#     factorial = factorial*i
# print(factorial) 

# from cmath import sqrt


# n = 100
# Sqsum = 0
# Tsum = 0
# for i in range(1,n+1):
#     Tsum += i
#     ts=Tsum**2
#     sqr = i**2
#     Sqsum  += sqr
# print(Sqsum )
# print(ts)
# print(ts - Sqsum)


# from array import array
# arr = array('i',[1,2,3,4,5])


# n = int(input("enter number :"))
# sum = 0
# for i in range(1,n):
#     if(n%i==0):
#         sum = sum +i
# if(sum == n):
#     print(f"{n} is a perfect numer")        
# else:
#     print("not a perfect number")

# str1 = input("enter string1:")
# str2 = input("enter string2:")
# if len(str1) != len(str2):
#     print("not a anagram string")
# else:
#     schar1 = sorted(str1)
#     schar2 = sorted(str2)  
# if schar1 == schar2:
#     print("strings are anagram") 
# else:
#     print("not a a anagram strings") 


#count vowels in string
# from itertools import count


# vowel = 'aeiou'
# str = input("enter string:")
# str = str.casefold()
# count = {}.fromkeys(vowel,0)

# for chr in str:
#     if chr in count:
#         count[chr] +=1
# print(count)

# X = [[1,2],[3,4],[5,6]]
# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
# for row in result:
#     print(row)

# from tkinter import Y


# X = [[1,2],[3,4],[5,6]]
# Y = [[1,2],[3,4],[5,6]]

# result = [[0,0],[0,0],[0,0]]
# #
# for i in range(len(X)):
#     for k in range(len(Y[0])):
#         for j in range(len(Y)):
#             result[i][j] += X[i][k]*Y[k][j]

# for row in result:
#     print(row)   


# with open("poem.binary", 'w') as f:
#     f.write("my name is sheela \n")
# for i in 'jhon':
#     if i == 'o':
#         pass
#     print(i,end=" ")


# for num in range(10,14):
#     for i  in range(2,num):
#         if num%i ==1:
#             print(num)
#             break

# a, b = 12, 5
# if a+b:
#     print(True)
# else:
#     print(False)

# from ast import Num
# from traceback import print_tb
# from unittest import result
# from xmlrpc.client import Boolean


# x = 0
# for i in range(10):
#     for j in range(-1,-10,-1):
#         x +=1
#         print(x)


# var = 10
# for i in range(10):
#     for j in range(2,10,1):
#         if var%2 == 0:
#             continue
#             var +=1
#     var +=1
# else:
#     var +=1
# print(var)   


# x = 0
# while(x<100):
#     x +=2
# print(x)
# 
# 
# x = 50
# y = 100
# print(x and y)   


# x = 10
# y = 50
# if x**2 < 100 and y<100:
#     print(x,y)
# else:
#     print("dev")   
# print(2**3**2)

# def add(a,b):
#     return a+5, b+5
# result = add(3,2)
# print(result)    

# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)
#     return a
# result = outer(5,10)
# print(result)  
# 

# def fun(num):
#     return num+25

# num= fun(5)
# print(num) 


#calculate days btw two dates  

# from datetime import date

# f_date = date(2014,7,2)
# l_date = date(2014,8,2)
# delay = l_date - f_date
# print(delay.days)


# import calendar

# cal = calendar.month(2022,3)
# print(cal)

# exam_st_date = (4,12,2022)
# print("the examination shedule:%i/%i/%i"%exam_st_date)

# def histogrsm(items):
#     for n in items:
#         output = ''
#         times = n
#         while(times>0):
#             output += '*'
#             times = times -1
#         print(output)    
# histogrsm([1,2,3,4,5,7])


#GCD
# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)

# a = 48
# b= 68

# print("the gcd of 68 and 48 is ",end="")
# print(hcf(a,b))

# import math

# gcd = math.gcd(68,48)
# print(gcd)





# import  os
# import platform

# print("name of the operating system",os.name)
# print("name of the operating system",platform.system())
# print("version of the operating system",platform.release())

# import multiprocessing
# print(multiprocessing.cpu_count())

# import os

# for data in  os.environ:
#     print(data)
#     print(os.environ[data])

# n = int(input("enter positive number:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum +i
# print(sum)    

# l = [23,55,55,667,88,88,1.34,12,12]
# sl = list[set(l)]
# print(sl)

str = "my name is dk "
print (str.count('m'))
      

















