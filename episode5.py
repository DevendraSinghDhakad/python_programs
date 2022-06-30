#find HCF

# def hcf(x,y):

#     if x>y:
#         smaller = y
#     else:
#         smaller = x

#     for i in range(1,smaller+1):
#         if((x%i==0)and(y%i==0)):
#             hcf = i
#     return hcf
# num1 = int(input("enter number1:"))
# num2 = int(input("enter number2:"))
# print("hcf of given numbers is " , hcf(num1,num2))      

# Python program to find GCD of two numbers

# def gcd(x, y):


#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             gcd = i 
#     return gcd

# num1 = 54 
# num2 = 24

# print("The GCD is", gcd(num1, num2))




# Python Program to find the L.C.M. of two input number

# def lcm(x, y):

   # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y

#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1

#    return lcm

# num1 = 54
# num2 = 24

# print("The L.C.M. is", lcm(num1, num2))


# from winreg import HKEY_CURRENT_CONFIG


# def gcd(x,y):
#     if x>y:
#         smaller  = y
#     else:
#        smaller = x

#     for i in range(1,smaller+1):
#         if((i%x==0)and(i%y==0)):
#             gcd=i
#     return gcd
# num1 =  24
# num2 = 48
# print("the hcf is",gcd(num1,num2))

# def quadrant(x, y):
#     if (x > 0 and y > 0):
#         print ("lies in First quadrant")
 
#     elif (x < 0 and y > 0):
#         print ("lies in Second quadrant")
         
#     elif (x < 0 and y < 0):
#         print ("lies in Third quadrant")
     
#     elif (x > 0 and y < 0):
#         print ("lies in Fourth quadrant")
# c1 = int(input("enter X-cordinate: "))
# c2 = int(input("enter Y-cordinate: "))

# quadrant(c1,c2)

# def factorial(num):
#     fact = 1
#     for i in range(num, 1, -1):
#         fact *= i
#     return fact




# n = int(input("Enter number of people: "))
# r = int(input("Enter number of seats: "))


# p = factorial(n) // factorial(n - r)


# print("Total possible arrangements:", p)

# n = int(input("enter number of peoples in room:"))
# no_of_handshake = int(n*(n-1)/2)
# print(f"maximum nuber of handshake possible {n} people are {no_of_handshake}")

#addition of fraction
# def findGCD(n1, n2):
#     gcd = 0
#     for i in range(1, int(min(n1, n2)) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             gcd = i
#     return gcd
# num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))
# num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))

# lcm = (den1 * den2) // findGCD(den1, den2)

# sum = (num1 * lcm // den1) + (num2 * lcm // den2)

# num3 = sum // findGCD(sum, lcm)

# lcm = lcm // findGCD(sum, lcm)

# print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", lcm)




#replace 0's with 1's
# from dataclasses import replace


# val = int(input("enter the number:"))
# val = str(val)
# replaced = val.replace('0','1')
# print(f"number after replacement is {replaced}") 

# def sum_of_primes(num):
#     isPrime = 1
#     for i in range (2,int(num/2),1):
#         if(num % i == 0):
#             isPrime = 0
#             break
#     return isPrime

# num = int(input("Enter a number : "))
# flag = 0;
# i = 2
# for i in range (2,int(num/2),1):
#     if(sum_of_primes(i) == 1):
#         if(sum_of_primes(num-i) == 1):
#             print(num,"can be expressed as the sum of",i,"and",num-i)
#             flag = 1;
# if (flag == 0):
#    print(f"{num} cannot be expressed as the sum of two prime numbers")

chr = input("enter character:")

if chr.lower() in  ('a','e','i','o','u'):
   print("given character is vowel")

elif chr.upper() in ('A','E','I','O','U'):
   print("given charactr is vowel")

else:
   print("given chacter  is cosonent ")    



