# from audioop import reverse


# n  = int(input("enter number to be reversed:"))
# rev = 0
# while n!=0:
#     y = n%10
#     rev = (rev*10)+y
#     n = n//10
# print(f"the reverse of given num is {rev}") 

#fabonacci series
# n = int(input("enter num:"))
# n1 = 0
# n2 = 1
# count = 0
# if n<=0:
#     print("enter correct number")

# else:
#     print("fabonacci series:")
#     while count<n:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count +=1

#factorial
# import math

# def factorial(n):
#     return (math.factorial(n))


# num  = int(input("enter num:"))
# print(print("Factorial of", num, "is",factorial(num)))



#find power of number
# def power(n, e):
#     if e == 0:
#         return 1
#     elif e == 1:
#         return n
#     else:
#         return (n*power(n, e-1))
# n = 4
# p = 2
# print(power(n, p))

#factor of number 

# n = int(input("enter num:"))
# factors = []

# for i in range(1,n+1):
#     if n%i==0:
#         factors.append(i)

# print(f"factors of {n}={factors}")

#check strong number 


# num=int(input("Enter a number:"))
# sum1=0
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     while(i<=r):
#         f=f*i
#         i=i+1
#     sum1=sum1+f
#     num=num//10
# if(sum1==temp):
#     print("The number is a strong number")
# else:
#     print("The number is not a strong number")


#perfect number 

#automhorphic number 

# n = int(input("enter number:"))
# sqr = n**2
# LD = sqr%10
# if LD == n:
#     print(f"given number is {n} automhorphic number")
# else:
#     print("not a automhorphic number")    


#harshad.....
# n=int(input("Enter a number:"))
# tot=0
# num = n
# while(num>0):
#     dig=num%10
#     tot=tot+dig
#     num = num//10
    
# if n%tot == 0:
#     print(f"given number is  harshad number")
# else:
#     print("not a harshad number!!")


#abundant nhumber

# n =  int(input("enter num:"))
# Fsum = 0
# for i in range(1,n):
#     if n%i==0:
#         Fsum = Fsum+i
# if Fsum>n:
#         print("given num is abundant number")
# else:
#     print("not a abundant number")
              

# freindly pair
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# sum1 = 0
# sum2 = 0
# for i in range(1,num1):
# 	if(num1 % i == 0):
# 		sum1 = sum1 + i
# for i in range(1,num2):
# 	if(num2 % i == 0):
# 		sum2 = sum2 + i
# if(sum1 == num1 and sum2 == num2):
# 	print("Friendly Pair")
# else:
# 	print("Not Friendly Pair")    
 
  















